def example(someIp=None, someString=None, **kwargs):
    """
    demo
    
    Args:
        someIp (CEF type: ip): Enter or map an IP here
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip)
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    someString.upper()
    
    outputs = {"outputIP":someIp, "outputString": someString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
