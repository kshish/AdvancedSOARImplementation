def july2023demo(someIP=None, someString=None, **kwargs):
    """
    demo
    
    Args:
        someIP (CEF type: ip): Map a IP(s) here
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): This is the resulting IP output from CF
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputIP=someIP
    outputString=someString
    
    outputs = {"outputIP": outputIP, "outputString": someString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
