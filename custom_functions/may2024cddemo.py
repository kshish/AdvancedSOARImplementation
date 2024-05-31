def may2024cddemo(someIp=None, someString=None, **kwargs):
    """
    demo of passthrough function
    
    Args:
        someIp (CEF type: ip): Map one or more IP
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): this should be same ip as inputed
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    internaloutputIP = someIp
    internaloutputString = someString
    
    
    
    outputs = {"outputIP": internaloutputIP, "outputString": internaloutputString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
