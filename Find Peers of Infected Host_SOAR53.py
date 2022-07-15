"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_infected_host_address' block
    get_infected_host_address(container=container)

    return

def search_for_peers(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("search_for_peers() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    query_formatted_string = phantom.format(
        container=container,
        template="""find_peers server={0}""",
        parameters=[
            "get_infected_host_address:custom_function_result.data.*.item"
        ])

    parameters = []

    if query_formatted_string is not None:
        parameters.append({
            "query": query_formatted_string,
            "command": "savedsearch",
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("run query", parameters=parameters, name="search_for_peers", assets=["splunk es"], callback=count_peers)

    return


def get_infected_host_address(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_infected_host_address() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.cef.destinationHostName","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "input_1": container_artifact_cef_item_0,
        "input_2": container_artifact_cef_item_1,
        "input_3": None,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="get_infected_host_address", callback=search_for_peers)

    return


def count_peers(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("count_peers() called")

    template = """Infected host communicated with {0} other hosts!"""

    # parameter list for template variable replacement
    parameters = [
        "search_for_peers:action_result.summary.total_events"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="count_peers")

    add_event_count_to_container(container=container)

    return


def add_event_count_to_container(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_event_count_to_container() called")

    count_peers = phantom.get_format_data(name="count_peers")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=count_peers)

    update_es_event_status(container=container)

    return


def update_es_event_status(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_es_event_status() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    comment_formatted_string = phantom.format(
        container=container,
        template="""Processing via SOAR: {0}\n""",
        parameters=[
            "container:url"
        ])

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.event_id","artifact:*.id"])

    parameters = []

    # build parameters list for 'update_es_event_status' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None:
            parameters.append({
                "comment": comment_formatted_string,
                "event_ids": container_artifact_item[0],
                "status": "in progress",
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update event", parameters=parameters, name="update_es_event_status", assets=["splunk es"], callback=save_peer_list)

    return


def save_peer_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("save_peer_list() called")

    id_value = container.get("id", None)
    search_for_peers_result_data = phantom.collect2(container=container, datapath=["search_for_peers:action_result.data.*.peer","search_for_peers:action_result.data.*.priority","search_for_peers:action_result.data.*.count","search_for_peers:action_result.parameter.context.artifact_id"], action_results=results)

    search_for_peers_result_item_0 = [item[0] for item in search_for_peers_result_data]
    search_for_peers_result_item_1 = [item[1] for item in search_for_peers_result_data]
    search_for_peers_result_item_2 = [item[2] for item in search_for_peers_result_data]

    parameters = []

    parameters.append({
        "peer": search_for_peers_result_item_0,
        "priority": search_for_peers_result_item_1,
        "count": search_for_peers_result_item_2,
        "container": id_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="kshish-phantom/L5_CF_Get_Query_Results_py3_SOAR53", parameters=parameters, name="save_peer_list", callback=playbook_create_events_for_peers_1)

    return


def playbook_create_events_for_peers_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_create_events_for_peers_1() called")

    save_peer_list__result = phantom.collect2(container=container, datapath=["save_peer_list:custom_function_result.data.results_list_name"])

    save_peer_list_data_results_list_name = [item[0] for item in save_peer_list__result]

    inputs = {
        "peerlist": save_peer_list_data_results_list_name,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "local/Create Events for Peers", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Create Events for Peers", container=container, inputs=inputs)

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return