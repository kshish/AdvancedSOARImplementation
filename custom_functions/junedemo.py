def junedemo(someIp=None, someString=None, **kwargs):
    """
    demo
    
    Args:
        someIp (CEF type: ip): Map IP(s) into this input
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): this is a passthrough IP 
        outputstring
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputIP = someIp
    outputstring = someString
    
    outputs = {"outputIP": outputIP, "outputstring": outputstring}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
