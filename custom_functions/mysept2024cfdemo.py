def mysept2024cfdemo(someIp=None, someString=None, **kwargs):
    """
    demo passthrough
    
    Args:
        someIp (CEF type: ip): map some ip into this variable
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIP (CEF type: ip): this is the ip from the input
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    
    ip=someIp
    mystring=someString
    
    
    
    
    
    
    outputs = {"outputIP": ip, "outputString": mystring}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
