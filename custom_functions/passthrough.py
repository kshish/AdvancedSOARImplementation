def passthrough(someIp=None, someHost=None, **kwargs):
    """
    simple demo
    
    Args:
        someIp (CEF type: ip): Map IP(s) into this input
        someHost
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): This is the modified input IP
        outputHost
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    
    
    
    
    outputs = {"outputIp": someIp, "outputHost": someHost}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
