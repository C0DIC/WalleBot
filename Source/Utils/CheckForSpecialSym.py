def checkSpecialSym(text) -> bool:
    if str(text).startswith('~'):
        return True
    return False


def isSndrSym(text) -> bool:
    if '@' in text:
        return True
    return False


def isTargetSym(text) -> bool:
    if '_' in text:
        return True
    return False
