def demo_noop_aug_2023(someIp=None, someString=None, **kwargs):
    """
    nice description
    
    Args:
        someIp (CEF type: ip): Map an IP (list) in here
        someString
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputIp (CEF type: ip): This is an IP
        outputString
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    outputIp=someIp
    outputString=someString
    
    outputs = {"outputIp": outputIp, "outputString": outputString}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
