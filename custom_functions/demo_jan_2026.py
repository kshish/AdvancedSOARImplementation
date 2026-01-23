def demo_jan_2026(some_ip=None, somestring=None, **kwargs):
    """
    this is a demo
    
    Args:
        some_ip (CEF type: ip): this argument will be blah blah
        somestring
    
    Returns a JSON-serializable object that implements the configured data paths:
        someoutputip (CEF type: ip)
        someoutputstring
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    someipvar=some_ip
    somestringvar=somestring
    
    a=23
    outputs={"someoutputip": someipvar, "someoutputstring": somestringvar}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
