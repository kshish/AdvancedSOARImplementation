def L5_MM_retrieveList(listName=None, **kwargs):
    """
    Args:
        listName
    
    Returns a JSON-serializable object that implements the configured data paths:
        listContents
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    read_list__peer_list = phantom.get_list(listName)[2]
    phantom.debug("from cf getlist")
    phantom.debug(read_list__peer_list)
    outputs = {"listContents": read_list__peer_list}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
