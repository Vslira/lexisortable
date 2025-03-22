import string
from math import log10
from typing import Union, Tuple, Optional


def _get_prefix_for_digits(digits: int) -> str:
    """Get the appropriate prefix character based on the number of digits."""
    if digits <= 26:  # a-z for 1-26 digits
        return string.ascii_lowercase[digits-1]
    
    # For numbers with more than 26 digits, use multiple letters
    # First letter cycles through a-z, second letter starts at 'a'
    quotient, remainder = divmod(digits-1, 26)
    return string.ascii_lowercase[remainder] + _get_prefix_for_digits(quotient+1)


def _get_digit_count(n: int) -> int:
    """Return the number of digits in a positive integer."""
    if n == 0:
        return 1
    return len(str(n))


def _split_float(f: float) -> Tuple[int, Optional[str]]:
    """Split a float into integer and decimal parts."""
    if f.is_integer():
        return int(f), None
    
    str_float = str(f)
    int_part, dec_part = str_float.split('.')
    # Remove trailing zeros from decimal part
    dec_part = dec_part.rstrip('0')
    
    return int(int_part), dec_part


def lexisort(n: Union[int, float]) -> str:
    """Convert a non-negative number to a lexicographically sortable string representation.
    
    Args:
        n: A non-negative integer or float to convert
        
    Returns:
        A string representation that sorts lexicographically
        in the same order as the numerical values.
        
    Raises:
        ValueError: If n is negative
    """
    # Check for negative numbers
    if n < 0:
        raise ValueError("lexisort only accepts non-negative numbers (>= 0)")
    
    # Handle floats
    if isinstance(n, float):
        int_part, dec_part = _split_float(n)
        
        if dec_part:
            # Get prefix based on integer part's digit count
            digit_count = _get_digit_count(int_part)
            char_prefix = _get_prefix_for_digits(digit_count)
            return f"{char_prefix}{int_part}p{dec_part}"
        else:
            # If there's no decimal part, treat as integer
            n = int_part
    
    # Handle integers
    digit_count = _get_digit_count(n)
    char_prefix = _get_prefix_for_digits(digit_count)
    
    return f"{char_prefix}{n}"


def delexisort(s: str) -> Union[int, float]:
    """Convert a lexicographically sortable string back to its original number.
    
    Args:
        s: A string representation created by lexisort
        
    Returns:
        The original non-negative number (int or float)
        
    Raises:
        ValueError: If the string format is invalid
    """
    # Find the first digit position
    for i, char in enumerate(s):
        if char.isdigit():
            break
    else:
        raise ValueError(f"Invalid lexisortable string: {s}")
    
    # Extract prefix and number part
    prefix = s[:i]
    number_part = s[i:]
    
    # Check if it's a float (contains 'p')
    if 'p' in number_part:
        int_part, dec_part = number_part.split('p')
        number = float(f"{int_part}.{dec_part}")
    else:
        number = int(number_part)
    
    return number
