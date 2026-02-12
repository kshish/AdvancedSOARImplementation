"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'sort_list_3' block
    sort_list_3(container=container)

    return

@phantom.playbook_block()
def sort_list_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("sort_list_3() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.id"])

    parameters = []

    # build parameters list for 'sort_list_3' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "unsorted_list": container_artifact_item[0],
            "sort_order": "a",
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="asi/sort_list", parameters=parameters, name="sort_list_3", callback=prompt_2)

    return


@phantom.playbook_block()
def prompt_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("prompt_2() called")

    # set approver and message variables for phantom.prompt call

    user = None
    role = "Administrator"
    message = """Here's the unsorted list:\n\n{0}\n\nHere's the sorted list: \n\n{1}"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.destinationAddress",
        "sort_list_3:custom_function_result.data.sorted_list"
    ]

    phantom.prompt2(container=container, user=user, role=role, message=message, respond_in_mins=30, name="prompt_2", parameters=parameters)

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