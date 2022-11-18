"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'demo_1' block
    demo_1(container=container)
    # call 'samplecf_2' block
    samplecf_2(container=container)

    return

def demo_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("demo_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.cef.destinationHostName","artifact:*.id"])

    parameters = []

    # build parameters list for 'demo_1' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "myIp": container_artifact_item[0],
            "somevalue": container_artifact_item[1],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="chris/demo", parameters=parameters, name="demo_1", callback=join_prompt_1)

    return


def join_prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_prompt_1() called")

    if phantom.completed(custom_function_names=["demo_1", "samplecf_2"]):
        # call connected block "prompt_1"
        prompt_1(container=container, handle=handle)

    return


def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = "admin"
    message = """{0}\n{1}\n{2}\n{3}\n"""

    # parameter list for template variable replacement
    parameters = [
        "demo_1:custom_function_result.data.myOutIP",
        "demo_1:custom_function_result.data.myout",
        "samplecf_2:custom_function_result.data.myoutIP",
        "samplecf_2:custom_function_result.data.someValueOut"
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters)

    return


def samplecf_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("samplecf_2() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.cef.destinationHostName","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "myIP": container_artifact_cef_item_0,
        "somevalue": container_artifact_cef_item_1,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="chris/sampleCF", parameters=parameters, name="samplecf_2", callback=join_prompt_1)

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