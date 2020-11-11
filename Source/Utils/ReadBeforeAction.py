def readBeforeAction(text):
    new_text = ''
    if text.startswith('['):
        for i in text:
            new_text += i
            if i == ']':
                break

    return new_text
