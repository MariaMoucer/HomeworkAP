# Function to calculate the length of the list
def length(lst):
    """
    Returns the number of elements in the list.
    
    Parameters:
    lst (list): The list whose length is to be calculated.

    Returns:
    int: The length of the list.
    """
    return len(lst)

# Function to calculate the mean (average) of the list
def mean(lst):
    """
    Calculates the arithmetic mean of the numbers in the list.
    
    Parameters:
    lst (list): The list of numbers.

    Returns:
    float: The mean of the numbers, or None if the list is empty.
    
    Raises:
    ValueError: If the list contains non-numeric values.
    """
    if len(lst) == 0:
        return None  # Return None for empty list
    try:
        return sum(lst) / len(lst)
    except TypeError:
        raise ValueError("List must contain only numeric values.")

# Function to calculate the range (max - min) of the list
def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    
    Parameters:
    lst (list): The list of numbers.

    Returns:
    int/float: The range of the list, or None if the list is empty.
    
    Raises:
    ValueError: If the list contains non-numeric values.
    """
    if len(lst) == 0:
        return None  # Return None for empty list
    try:
        return max(lst) - min(lst)
    except TypeError:
        raise ValueError("List must contain only numeric values.")
