"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'july2023demo_1' block
    july2023demo_1(container=container)

    return

@phantom.playbook_block()
def july2023demo_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("july2023demo_1() called")

    name_value = container.get("name", None)
    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.destination","artifact:*.id"])

    parameters = []

    # build parameters list for 'july2023demo_1' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "someIP": container_artifact_item[0],
            "someString": name_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="chris/july2023demo", parameters=parameters, name="july2023demo_1", callback=prompt_1)

    return


@phantom.playbook_block()
def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = None
    role = "Administrator"
    message = """same IP {0}\nEvent Name {1}"""

    # parameter list for template variable replacement
    parameters = [
        "july2023demo_1:custom_function_result.data.outputIP",
        "container:name"
    ]

    # responses
    response_types = [
        {
            "prompt": "Enter a container ID",
            "options": {
                "type": "message",
            },
        }
    ]

    phantom.prompt2(container=container, user=user, role=role, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters, response_types=response_types, callback=get_data_1)

    return


@phantom.playbook_block()
def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    location_formatted_string = phantom.format(
        container=container,
        template="""container/{0}\n""",
        parameters=[
            "prompt_1:action_result.summary.responses.0"
        ])

    prompt_1_result_data = phantom.collect2(container=container, datapath=["prompt_1:action_result.summary.responses.0","prompt_1:action_result.parameter.context.artifact_id"], action_results=results)

    parameters = []

    # build parameters list for 'get_data_1' call
    for prompt_1_result_item in prompt_1_result_data:
        if location_formatted_string is not None:
            parameters.append({
                "location": location_formatted_string,
                "context": {'artifact_id': prompt_1_result_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_data_1", assets=["soar100"], callback=prompt_2)

    return


@phantom.playbook_block()
def prompt_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("prompt_2() called")

    # set user and message variables for phantom.prompt call

    user = None
    role = "Administrator"
    message = """name: {0}\ndescription: {1}\nResponse body \n{2}"""

    # parameter list for template variable replacement
    parameters = [
        "get_data_1:action_result.data.*.response_body.name",
        "get_data_1:action_result.data.*.parsed_response_body.description",
        "get_data_1:action_result.data.*.parsed_response_body"
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