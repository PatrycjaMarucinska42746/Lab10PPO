def text_convert_gurad(text):
    try:
        n = float(text)
        return True
    except ValueError:
        return False
    
def split_guard(text, sep):
    if sep not in text:
        return False

    arrays = text.split(sep)
    return len(arrays) == 2 and all(arrays)