def merge_and_analyze_lists(primary_list, secondary_list, sort=True, reverse=False):
    """_summary_

    Args:
        primary_list (_type_): _description_
        secondary_list (_type_): _description_
        sort (bool, optional): _description_. Defaults to True.
        reverse (bool, optional): _description_. Defaults to False.

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if not isinstance(primary_list, list) or not isinstance(secondary_list, list):
        raise ValueError("Both arguments must be of type 'list'")
    
    merged_list = primary_list + secondary_list
    
    if sort:
        merged_list = sorted(merged_list, reverse=reverse)
    
    total_elements = len(merged_list)
    unique_elements = len(set(merged_list))
    first_element = merged_list[0]
    last_element = merged_list[-1]
    
    return {
        'total_elements': total_elements,
        'unique_elements': unique_elements,
        'first_element': first_element,
        'last_element': last_element
    }