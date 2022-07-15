"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'retrieve_list' block
    retrieve_list(container=container)

    return

def retrieve_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("retrieve_list() called")

    playbook_input_peerlist = phantom.collect2(container=container, datapath=["playbook_input:peerlist"])

    parameters = []

    # build parameters list for 'retrieve_list' call
    for playbook_input_peerlist_item in playbook_input_peerlist:
        parameters.append({
            "listName": playbook_input_peerlist_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="kshish-phantom/L5_CF_Retrieve_List_SOAR53", parameters=parameters, name="retrieve_list", callback=filter_list)

    return


def create_containers(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_containers() called")

    label_value = container.get("label", None)
    filter_list__result = phantom.collect2(container=container, datapath=["filter_list:custom_function_result.data.filtered_list"])

    filter_list_data_filtered_list = [item[0] for item in filter_list__result]

    parameters = []

    parameters.append({
        "container_label": label_value,
        "to_be_containerized": filter_list_data_filtered_list,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="kshish-phantom/L5_CF_Create_Containers_From_List_py3_SOAR53", parameters=parameters, name="create_containers")

    return


def filter_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_list() called")

    retrieve_list__result = phantom.collect2(container=container, datapath=["retrieve_list:custom_function_result.data.listContents"])

    retrieve_list_data_listcontents = [item[0] for item in retrieve_list__result]

    parameters = []

    parameters.append({
        "filter_items": "high,critical",
        "list_obj": retrieve_list_data_listcontents,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/L5_CF_Filter_List_copy_by_scott", parameters=parameters, name="filter_list", callback=create_containers)

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