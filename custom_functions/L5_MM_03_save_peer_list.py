def L5_MM_03_save_peer_list(peer=None, priority=None, count=None, container_id=None, **kwargs):
    """
    Args:
        peer
        priority
        count
        container_id (CEF type: phantom container id)
    
    Returns a JSON-serializable object that implements the configured data paths:
        result_list_name
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(container_id)
    phantom.debug(type(container_id))
    list_name = "temp_peer_list_%s" % container_id
    
    # You need the container object in order to update it.
    update_container = phantom.get_container(container_id)
    
    # Get the data node of the container
    data = phantom.get_container(container_id)['data']
    data.update({"peer_list":list_name})
    phantom.update(update_container, {'data':data} )
    phantom.remove_list(list_name)
    
    for i in range(0,len(peer)):
        phantom.add_list(list_name, [peer[i],priority[i],count[i]])
    
    # The actual list is in slot 3 of the tuple returned by phantom.get_list()
    results_list = phantom.get_list(list_name)[2]
    #phantom.debug(results_list)
    outputs = {'result_list_name': list_name}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
