def sampleCF(myIP=None, somevalue=None, **kwargs):
    """
    this is a demo
    
    Args:
        myIP (CEF type: ip): Map an IP or IP list here
        somevalue
    
    Returns a JSON-serializable object that implements the configured data paths:
        myoutIP (CEF type: ip): some output ip 
        someValueOut
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputs = {"myoutIP":myIP,"someValueOut":somevalue}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
