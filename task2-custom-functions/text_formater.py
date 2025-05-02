def format_text(txt: str, prefix: str = "", suffix: str = "", capitalize: bool = False, max_length: int = None) -> str:
    """
    Formats the given string according to the parameters.
    
    Args:
        txt (str): The input string to format.
        prefix (str, optional): A string to add to the beginning of the text. (default is "")
        suffix (str, optional): A string to add to the end of the text. (default is "")
        capitalize (bool, optional): If True, capitalizes the first character of the text. (default is False)
        max_length (int, optional): The maximum allowed length of the final text. (default is None, meaning no limit.)
        
    Returns:
        str: The formatted text.

    Raises:
        TypeError: If any input is of an incorrect type.
        ValueError: If max_length is negative.
    """
    # Type checks
    if not isinstance(txt, str):
        raise TypeError("The 'txt' parameter must be a string.")
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' parameter must be a string.")
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' parameter must be a string.")
    if not isinstance(capitalize, bool):
        raise TypeError("The 'capitalize' parameter must be a boolean.")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' must be an integer or None.")
        if max_length < 0:
            raise ValueError("The 'max_length' must be positive.")

    # Apply prefix and suffix
    formatted_text = f"{prefix}{txt}{suffix}"

    # Apply capitalization
    if capitalize:
        formatted_text = formatted_text.capitalize()

    # Apply maximum length
    if max_length is not None and len(formatted_text) > max_length:
        formatted_text = formatted_text[:max_length]
    return formatted_text
result = format_text("kigali", prefix="Dr.", suffix="?", capitalize=True, max_length=70)
print(result)

