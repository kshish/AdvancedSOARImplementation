def nov_2024_cf_passthrough_demo(someIp=None, someString=None, **kwargs):
    """
    demo
    
    Args:
        someIp (CEF type: ip): This input will get passed through as output
        someString: any string
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): this is the same IP as was passed in
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    
    
    myIp=someIp
    myString=someString
    
    
    
    
    outputs = {"outputIp": myIp, "outputString": myString}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
