def myMarchCFDemo(myIP=None, someString=None, **kwargs):
    """
    chris wuz here demoing
    
    Args:
        myIP (CEF type: ip): More info
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        myOutIP (CEF type: ip): this has none, one, or more IPs 
        myoutputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    outputs = {"myOutIP": myIP, "myoutputString": someString }
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
