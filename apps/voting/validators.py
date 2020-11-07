def validate_length(value):
    if len(value) == 64:
        return value
    else:
        raise ValueError("Wrong format for Hashing algorithm")
