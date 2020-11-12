def checkSpecialSym(text) -> bool:
    if str(text).startswith('~'):
        return True
    return False


def checkForSndrSyms(text) -> bool:
    if "@" in text:
        return True
    return False


def checkForTargetSyms(text) -> bool:
    if "#" in text:
        return True
    return False
