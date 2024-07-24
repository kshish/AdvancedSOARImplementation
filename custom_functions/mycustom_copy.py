def mycustom_copy(someIp=None, someString=None, **kwargs):
    """
    this is a demo
    
    Args:
        someIp (CEF type: ip): Map one or more IPs into this input
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): this is the output IP from CF
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    outputs = {"outputIP": someIp, "outputString": someString}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
