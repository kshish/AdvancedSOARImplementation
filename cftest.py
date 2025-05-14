"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'cf_2025_mar_passthrough_demo_1' block
    cf_2025_mar_passthrough_demo_1(container=container)

    return

@phantom.playbook_block()
def cf_2025_mar_passthrough_demo_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("cf_2025_mar_passthrough_demo_1() called")

    name_value = container.get("name", None)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destination","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "someIp": container_artifact_cef_item_0,
        "someString": name_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="chris/cf_2025_mar_passthrough_demo", parameters=parameters, name="cf_2025_mar_passthrough_demo_1", callback=prompt_1)

    return


@phantom.playbook_block()
def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = "soardev"
    role = None
    message = """{0}\n{1}\n"""

    # parameter list for template variable replacement
    parameters = [
        "cf_2025_mar_passthrough_demo_1:custom_function_result.data.outputIp",
        "cf_2025_mar_passthrough_demo_1:custom_function_result.data.outputString"
    ]

    phantom.prompt2(container=container, user=user, role=role, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters)

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