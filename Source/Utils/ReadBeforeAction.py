def readBeforeAction(text):
    new_text = ''
    if '[' in text or ']' in text:
        for i in text:
            if i == '[':
                new_text += i
            if i != ']':
                new_text += i
            else:
                break
    return new_text
