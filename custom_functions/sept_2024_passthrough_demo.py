def sept_2024_passthrough_demo(someIp=None, someString=None, **kwargs):
    """
    this is a demo
    
    Args:
        someIp (CEF type: ip): Map some IP(s) into this input variable
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): this is the output ... in this case the same value as input ip
        outputString
        success
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    
    
    
    
    
    
    
    
    
    
    
    success_code="error"
    
    
    outputs={"outputIp": someIp, "outputString": someString, "success": success_code }
    
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
