def cf_2025_mar_passthrough_demo(someIp=None, someString=None, **kwargs):
    """
    this is a demo
    
    Args:
        someIp (CEF type: ip): Provide one or more Ip(s)
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): This is the IP(s) returned from my cf
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    myoutputIp=someIp
    
    myoutputstring=someString.upper()
    
    
    
    
    outputs={"outputIp": myoutputIp, "outputString": myoutputstring}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
