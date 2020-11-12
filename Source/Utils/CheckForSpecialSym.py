def checkSpecialSym(text) -> bool:
    if str(text).startswith('//'):
        return True
    return False


def checkForSndrSyms(text) -> bool:
    if "@s" in text:
        return True
    return False


def checkForTargetSyms(text) -> bool:
    if "@y" in text:
        return True
    return False
