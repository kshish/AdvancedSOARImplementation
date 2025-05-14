def may_2025_demo(myDestination=None, myPriority=None, **kwargs):
    """
    simple passthrough demo
    
    Args:
        myDestination: map some ip into this input
        myPriority: map a priority that will get increased to next level
    
    Returns a JSON-serializable object that implements the configured data paths:
        outputDestination
        newPriority: one level higher
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    
    tempOutDest = myDestination 
    tempOutPriority = "critical"
    
    
    phantom.debug(tempOutDest)
    phantom.debug(myDestination)
    
    
    
    
    
    
    
    
    
    outputs = {"outputDestination": myDestination , "newPriority": tempOutPriority}
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
