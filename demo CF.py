"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'demopassthrough_1' block
    demopassthrough_1(container=container)

    return

@phantom.playbook_block()
def demopassthrough_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("demopassthrough_1() called")

    name_value = container.get("name", None)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.id"])

    parameters = []

    # build parameters list for 'demopassthrough_1' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "someIp": container_artifact_item[0],
            "someString": name_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="chris/demopassthrough", parameters=parameters, name="demopassthrough_1", callback=prompt_1)

    return


@phantom.playbook_block()
def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = None
    role = "Administrator"
    message = """IP {0}\nstring {1}"""

    # parameter list for template variable replacement
    parameters = [
        "demopassthrough_1:custom_function_result.data.outputIp",
        "demopassthrough_1:custom_function_result.data.outputString"
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