def demo_cf_passthrough(my_ip_used_for_something=None, myString=None, **kwargs):
    """
    This is a demo of a cf
    
    
    
    
    Args:
        my_ip_used_for_something (CEF type: ip): map an ip in here to get passed through as output
        myString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip)
        myOutputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    myvar=my_ip_used_for_something
    myothervar=myString
    
    
    
    outputs={"outputIP": myvar, "myOutputString": myothervar}
    
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
