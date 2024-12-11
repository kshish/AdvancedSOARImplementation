def dec11_trim_last_3(stringvar=None, **kwargs):
    """
    This CF will trim the last three character off the input parameter.
    
    Args:
        stringvar: The input will have last three characters stripped out.
    
    Returns a JSON-serializable object that implements the configured data paths:
        trimmed_string: Trimmed off last three character
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    trimmed_string=stringvar[:-3]
    
    outputs = {"trimmed_string": trimmed_string}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
