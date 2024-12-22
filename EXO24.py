def anagrams(str1, str2):
    """
    Returns True if str1 and str2 are anagrams, False otherwise.
    
    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    bool: True if str1 and str2 are anagrams, False otherwise.
    """
    # If the strings have different lengths, they can't be anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)
