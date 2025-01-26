
def remove_suffix(string, suffix):
    # remove a certain suffix in a string if it has it, do nothing if it does not
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string


