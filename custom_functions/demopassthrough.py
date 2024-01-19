def demopassthrough(someIp=None, someString=None, **kwargs):
    """
    demo
    
    Args:
        someIp (CEF type: ip): Map an IP into this input parameter
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): This is the output IP
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    
    
    
    outputs = {"outputIp": someIp, "outputString": someString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
