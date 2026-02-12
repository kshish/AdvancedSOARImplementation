def sort_list(unsorted_list=None, **kwargs):
    """
    Sort a list
    
    Args:
        unsorted_list
    
    Returns a JSON-serializable object that implements the configured data paths:
        sorted_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    sorted_list=unsorted_list



# Default to ascending
    sorted_list=sorted(unsorted_list, reverse=False)
    
    outputs={"sorted_list": sorted_list }
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
