"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'l5_mm_retrievelist_1' block
    l5_mm_retrievelist_1(container=container)

    return

def l5_mm_retrievelist_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_mm_retrievelist_1() called")

    playbook_input_peer_list_name = phantom.collect2(container=container, datapath=["playbook_input:peer_list_name"])

    parameters = []

    # build parameters list for 'l5_mm_retrievelist_1' call
    for playbook_input_peer_list_name_item in playbook_input_peer_list_name:
        parameters.append({
            "listName": playbook_input_peer_list_name_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/L5_MM_retrieveList", parameters=parameters, name="l5_mm_retrievelist_1", callback=filter_1)

    return


def l5_mm_create_containers_from_list_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("l5_mm_create_containers_from_list_2() called")

    l5_mm_retrievelist_1__result = phantom.collect2(container=container, datapath=["l5_mm_retrievelist_1:custom_function_result.data.listContents"])

    l5_mm_retrievelist_1_data_listcontents = [item[0] for item in l5_mm_retrievelist_1__result]

    parameters = []

    parameters.append({
        "container_label": "notable",
        "to_be_containerized": l5_mm_retrievelist_1_data_listcontents,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/L5_MM_Create_containers_from_list", parameters=parameters, name="l5_mm_create_containers_from_list_2")

    return


def debug_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_3() called")

    l5_mm_retrievelist_1_data_listcontents = phantom.collect2(container=container, datapath=["l5_mm_retrievelist_1:custom_function_result.data.listContents.*.peer","l5_mm_retrievelist_1:custom_function_result.data.listContents.*.priority","l5_mm_retrievelist_1:custom_function_result.data.listContents.*.count"])

    l5_mm_retrievelist_1_data_listcontents___peer = [item[0] for item in l5_mm_retrievelist_1_data_listcontents]
    l5_mm_retrievelist_1_data_listcontents___priority = [item[1] for item in l5_mm_retrievelist_1_data_listcontents]
    l5_mm_retrievelist_1_data_listcontents___count = [item[2] for item in l5_mm_retrievelist_1_data_listcontents]

    parameters = []

    parameters.append({
        "input_1": None,
        "input_2": l5_mm_retrievelist_1_data_listcontents___peer,
        "input_3": l5_mm_retrievelist_1_data_listcontents___priority,
        "input_4": l5_mm_retrievelist_1_data_listcontents___count,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_3")

    return


def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["l5_mm_retrievelist_1:custom_function_result.data.listContents.*.priority", "==", "high"]
        ],
        name="filter_1:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        l5_mm_create_containers_from_list_2(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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