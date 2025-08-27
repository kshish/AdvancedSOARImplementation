"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'cf_demo_2025_aug_1' block
    cf_demo_2025_aug_1(container=container)

    return

@phantom.playbook_block()
def cf_demo_2025_aug_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("cf_demo_2025_aug_1() called")

    name_value = container.get("name", None)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destination","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "ip": container_artifact_cef_item_0,
        "container_name": name_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="adv/cf_demo_2025_aug", parameters=parameters, name="cf_demo_2025_aug_1", callback=prompt_1)

    return


@phantom.playbook_block()
def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = "soar_local_admin"
    role = None
    message = """out IP: {0}\ncontainer name: {1}"""

    # parameter list for template variable replacement
    parameters = [
        "cf_demo_2025_aug_1:custom_function_result.data.outip",
        "cf_demo_2025_aug_1:custom_function_result.data.outcontainer"
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