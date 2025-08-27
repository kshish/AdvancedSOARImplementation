def cf_demo_2025_aug(ip=None, container_name=None, **kwargs):
    """
    this i s demo of a custom function
    
    Args:
        ip (CEF type: ip): Provide one or more IPs
        container_name
    
    Returns a JSON-serializable object that implements the configured data paths:
        outip (CEF type: ip): This is the result of the cf doing something
        outcontainer
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    someip=ip
    outcontainer=container_name.upper()
    
    outputs = {"outip":someip, "outcontainer": outcontainer}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
