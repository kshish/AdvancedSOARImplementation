def demo(myIp=None, somevalue=None, **kwargs):
    """
    demo
    
    Args:
        myIp (CEF type: ip): Please map ip(s) into this parameter
        somevalue
    
    Returns a JSON-serializable object that implements the configured data paths:
        myOutIP (CEF type: ip): Outputs ip(s) as datatype
        myout
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...

    outputs = {"myOutIp":myIp,"myOut":somevalue}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
