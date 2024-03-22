def demo_passthrough(someIp=None, someString=None, **kwargs):
    """
    demo of CF
    
    Args:
        someIp (CEF type: ip): Map IP(s) into this input variable
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): This will be IP(s)
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputIp=someIp
    outputString=someString
    
    outputs = {"outputIp": outputIp, "outputString": outputString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
