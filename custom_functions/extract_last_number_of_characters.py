def extract_last_number_of_characters(some_string=None, number_of_characters=None, **kwargs):
    """
    This is a cf that extracts number of remaining characters from a string
    
    Args:
        some_string: Provide the string whose last number of characters you want to extract
        number_of_characters: blah blhah dsfgqasasdfasf
    
    Returns a JSON-serializable object that implements the configured data paths:
        string_output: the last bunch of characters from string input
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    tempstring = some_string[:number_of_characters]
    outputs = {"string_output": tempstring}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
