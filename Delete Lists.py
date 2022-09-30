"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_lists' block
    get_lists(container=container)

    return

def get_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_lists() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    parameters.append({
        "location": "/decided_list?_filter_name__startswith=\"temp_\"",
        "verify_certificate": False,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_lists", assets=["es03"], callback=format_list_name)

    return


def debug_show_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_show_lists() called")

    get_lists_result_data = phantom.collect2(container=container, datapath=["get_lists:action_result.data.*.response_body","get_lists:action_result.message","get_lists:action_result.data.*.response_body.data.*.name","get_lists:action_result.data.*.response_body.data.*.name.*","get_lists:action_result.data.*.parsed_response_body.*","get_lists:action_result.data.*.parsed_response_body.data.*.name","get_lists:action_result.parameter.context.artifact_id"], action_results=results)

    get_lists_result_item_0 = [item[0] for item in get_lists_result_data]
    get_lists_result_message = [item[1] for item in get_lists_result_data]
    get_lists_result_item_2 = [item[2] for item in get_lists_result_data]
    get_lists_result_item_3 = [item[3] for item in get_lists_result_data]
    get_lists_result_item_4 = [item[4] for item in get_lists_result_data]
    get_lists_result_item_5 = [item[5] for item in get_lists_result_data]

    parameters = []

    parameters.append({
        "input_1": get_lists_result_item_0,
        "input_2": get_lists_result_message,
        "input_3": get_lists_result_item_2,
        "input_4": get_lists_result_item_3,
        "input_5": get_lists_result_item_4,
        "input_6": get_lists_result_item_5,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_show_lists", callback=delete_lists)

    return


def remove_list_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("remove_list_2() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.remove_list(list_name="temp_peer_list_29")

    return


def list_merge_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("list_merge_3() called")

    get_lists_result_data = phantom.collect2(container=container, datapath=["get_lists:action_result.data.*.response_body.data.*.name","get_lists:action_result.parameter.context.artifact_id"], action_results=results)

    get_lists_result_item_0 = [item[0] for item in get_lists_result_data]

    parameters = []

    parameters.append({
        "input_1": get_lists_result_item_0,
        "input_2": None,
        "input_3": None,
        "input_4": None,
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

    phantom.custom_function(custom_function="community/list_merge", parameters=parameters, name="list_merge_3")

    return


def show_value(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("show_value() called")

    format_list_name__as_list = phantom.get_format_data(name="format_list_name__as_list")
    format_list_name__as_list = phantom.get_format_data(name="format_list_name__as_list")
    format_list_name__as_list = phantom.get_format_data(name="format_list_name__as_list")

    parameters = []

    parameters.append({
        "input_1": format_list_name__as_list,
        "input_2": format_list_name__as_list,
        "input_3": format_list_name__as_list,
        "input_4": None,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="show_value")

    return


def format_list_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_list_name() called")

    template = """%%\ndecided_list/{0}\n%%"""

    # parameter list for template variable replacement
    parameters = [
        "get_lists:action_result.data.*.response_body.data.*.name"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_list_name")

    debug_show_lists(container=container)

    return


def delete_temp_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("delete_temp_lists() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    location_formatted_string = phantom.format(
        container=container,
        template="""{0}""",
        parameters=[
            "get_lists:action_result.data.*.parsed_response_body.data.*.name"
        ])

    ################################################################################
    # decided_list?_filter_name__startswith=%22temp_%22
    ################################################################################

    parameters = []

    if location_formatted_string is not None:
        parameters.append({
            "location": location_formatted_string,
            "verify_certificate": False,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("delete data", parameters=parameters, name="delete_temp_lists", assets=["es03"])

    return


def delete_lists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("delete_lists() called")

    get_lists_result_data = phantom.collect2(container=container, datapath=["get_lists:action_result.data.*.parsed_response_body"], action_results=results)

    get_lists_result_item_0 = [item[0] for item in get_lists_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(get_lists_result_data[0][0])
    for item in get_lists_result_data[0][0]['data']:
        phantom.debug(item['name'])
        
        phantom.remove_list(item['name'])
    
    ################################################################################
    ## Custom Code End
    ################################################################################

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