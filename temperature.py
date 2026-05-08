def is_overheating(temp_c):
    """Return True if temperature exceeds safe limit."""
    if temp_c < 0:
        raise ValueError("Reading error")
    return temp_c > 85