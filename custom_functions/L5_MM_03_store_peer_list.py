def L5_MM_03_store_peer_list(container_id=None, peer_list=None, **kwargs):
    """
    Use this only if you know python very well. Otherwise use "L5_MM_03_save_peer_list" custom function instead
    
    Args:
        container_id (CEF type: phantom container id)
        peer_list
    
    Returns a JSON-serializable object that implements the configured data paths:
        new_list_name
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(container_id)
    phantom.debug(type(container_id))
    new_list_name = "temp_peer_list_%s" % container_id
    
    # You need the container object in order to update it.
    update_container = phantom.get_container(container_id)
    
    # Get the data node of the container
    data = phantom.get_container(container_id)['data']
    
    data.update({"temp_peer_list":new_list_name})
    phantom.update(update_container, {'data':data} )
    phantom.remove_list(new_list_name)
    
    for i in range(0,len(peer_list[0]['data'])):
        phantom.debug(len(peer_list[0]['data']))
        #peer_priority = peer_list[i]['priority']
        #if peer_priority == 'critical' or peer_priority == 'high':
        #phantom.add_list(new_list_name, [peer_list['data'][i]['peer'],peer_list['data'][i]['priority'],peer_list['data'][i]['count']])
    
    # The actual list is in slot 3 of the tuple returned by phantom.get_list()
    results_list = phantom.get_list(new_list_name)[2]
    phantom.debug(results_list)
    outputs = {'new_list_name': new_list_name}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
