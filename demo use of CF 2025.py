"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'passthrough_2025_feb_4' block
    passthrough_2025_feb_4(container=container)

    return

@phantom.playbook_block()
def passthrough_2025_feb_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("passthrough_2025_feb_4() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destinationAddress","artifact:*.cef.destinationHostName","artifact:*.id"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]
    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "Ip_input": container_artifact_cef_item_0,
        "someString_input": container_artifact_cef_item_1,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="Chris/passthrough_2025_feb", parameters=parameters, name="passthrough_2025_feb_4", callback=add_comment_1)

    return


@phantom.playbook_block()
def add_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_comment_1() called")

    passthrough_2025_feb_4__result = phantom.collect2(container=container, datapath=["passthrough_2025_feb_4:custom_function_result.data.Ip_output"])

    passthrough_2025_feb_4_data_ip_output = [item[0] for item in passthrough_2025_feb_4__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=passthrough_2025_feb_4_data_ip_output)

    add_comment_5(container=container)

    return


@phantom.playbook_block()
def add_comment_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_comment_5() called")

    passthrough_2025_feb_4__result = phantom.collect2(container=container, datapath=["passthrough_2025_feb_4:custom_function_result.data.string_output"])

    passthrough_2025_feb_4_data_string_output = [item[0] for item in passthrough_2025_feb_4__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=passthrough_2025_feb_4_data_string_output)

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