def last_x_characters(someString=None, number_of_characters=None, **kwargs):
    """
    This CF returns the last three characters of a input 
    
    Args:
        someString
        number_of_characters: Provide a number of characters from the end of the string that you want returned
    
    Returns a JSON-serializable object that implements the configured data paths:
        output_string: this is the last few character of the input string
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    output_string = someString[:number_of_characters]
    
    outputs={"output_string": output_string}
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
