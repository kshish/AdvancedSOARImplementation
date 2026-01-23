"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'format_1' block
    format_1(container=container)

    return

@phantom.playbook_block()
def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("run_query_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_1 = phantom.get_format_data(name="format_1")

    parameters = []

    if format_1 is not None:
        parameters.append({
            "query": format_1,
            "command": "savedsearch",
            "end_time": "now",
            "start_time": "-15m",
            "search_mode": "smart",
            "add_raw_field": True,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("run query", parameters=parameters, name="run_query_1", assets=["instructors es"], callback=run_query_1_callback)

    return


@phantom.playbook_block()
def run_query_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("run_query_1_callback() called")

    
    filter_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    debug_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


@phantom.playbook_block()
def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_1() called")

    template = """find_peers server=\"{0}\"\n"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destination"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    run_query_1(container=container)

    return


@phantom.playbook_block()
def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        logical_operator="or",
        conditions=[
            ["run_query_1:action_result.data.*.priority", "==", "critical"],
            ["run_query_1:action_result.data.*.priority", "==", "high"],
            ["run_query_1:action_result.data.*.priority", "==", "low"],
            ["run_query_1:action_result.data.*.priority", "==", "medium"]
        ],
        conditions_dps=[
            ["run_query_1:action_result.data.*.priority", "==", "critical"],
            ["run_query_1:action_result.data.*.priority", "==", "high"],
            ["run_query_1:action_result.data.*.priority", "==", "low"],
            ["run_query_1:action_result.data.*.priority", "==", "medium"]
        ],
        name="filter_1:condition_1",
        case_sensitive=False,
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        format_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_2() called")

    template = """There were a total of {0} peers that {1} communicated with. Here is a list of the high and critical priority peers.\n"""

    # parameter list for template variable replacement
    parameters = [
        "run_query_1:action_result.summary.total_events",
        "artifact:*.cef.destination"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    format_3(container=container)

    return


@phantom.playbook_block()
def format_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_3() called")

    template = """%%\nPeer: {0} with priority {1} communicated {2} times\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_1:condition_1:run_query_1:action_result.data.*.peer",
        "filtered-data:filter_1:condition_1:run_query_1:action_result.data.*.priority",
        "filtered-data:filter_1:condition_1:run_query_1:action_result.data.*.count"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_3")

    format_4(container=container)

    return


@phantom.playbook_block()
def format_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_4() called")

    template = """{0}\n{1}\n"""

    # parameter list for template variable replacement
    parameters = [
        "format_2:formatted_data",
        "format_3:formatted_data"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_4")

    list_merge_1(container=container)

    return


@phantom.playbook_block()
def update_event_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("update_event_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    list_merge_1__result = phantom.collect2(container=container, datapath=["list_merge_1:custom_function_result.data.item"])
    format_4 = phantom.get_format_data(name="format_4")

    parameters = []

    # build parameters list for 'update_event_1' call
    for list_merge_1__result_item in list_merge_1__result:
        if list_merge_1__result_item[0] is not None:
            parameters.append({
                "status": "in progress",
                "comment": format_4,
                "event_ids": list_merge_1__result_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update event", parameters=parameters, name="update_event_1", assets=["instructors es"])

    return


@phantom.playbook_block()
def list_merge_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("list_merge_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.notableId","artifact:*.cef.event_id","artifact:*.id"])

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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_1", callback=update_event_1)

    return


@phantom.playbook_block()
def debug_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("debug_2() called")

    run_query_1_result_data = phantom.collect2(container=container, datapath=["run_query_1:action_result.data","run_query_1:action_result.parameter.context.artifact_id"], action_results=results)

    run_query_1_result_item_0 = [item[0] for item in run_query_1_result_data]

    parameters = []

    parameters.append({
        "input_1": run_query_1_result_item_0,
        "input_2": None,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_2")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return