"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'format_1' block
    format_1(container=container)

    return

def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("run_query_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_1 = phantom.get_format_data(name="format_1")

    parameters = []

    if format_1 is not None:
        parameters.append({
            "command": "savedsearch",
            "query": format_1,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("run query", parameters=parameters, name="run_query_1", assets=["splunk100"], callback=filter_1)

    return


def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_1() called")

    template = """find_peers server=\"{0}\"\n"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destinationHostName"
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


def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["run_query_1:action_result.data.*.priority", "==", "critical"]
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        format_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_2() called")

    template = """%%\nPeer: {0} communicated with {1}, with severity {2}, {3} times\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destinationHostName",
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

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    prompt_1(container=container)

    return


def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = "admin"
    message = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "format_2:formatted_data"
    ]

    # responses
    response_types = [
        {
            "prompt": "Would you like to change status of Notable?",
            "options": {
                "type": "list",
                "choices": [
                    "Yes",
                    "No"
                ],
            },
        }
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters, response_types=response_types, callback=decision_1)

    return


def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["prompt_1:action_result.summary.responses.0", "==", "Yes"]
        ])

    # call connected blocks if condition 1 matched
    if found_match_1:
        update_event_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


def update_event_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_event_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.notableId","artifact:*.id"])
    format_2 = phantom.get_format_data(name="format_2")

    parameters = []

    # build parameters list for 'update_event_1' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None:
            parameters.append({
                "status": "in progress",
                "comment": format_2,
                "event_ids": container_artifact_item[0],
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("update event", parameters=parameters, name="update_event_1", assets=["splunk100"])

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