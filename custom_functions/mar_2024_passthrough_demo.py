def mar_2024_passthrough_demo(someIp=None, someString=None, **kwargs):
    """
    demo
    
    Args:
        someIp (CEF type: ip): Map IP(s) here
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): this is IP(s)
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputIP=someIp
    outputString=someString
    
    outputs = {"outputIP" : outputIP, "outputString" : outputString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
