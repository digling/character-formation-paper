from sinopy import parse_baxter, parse_chinese_morphemes, baxter2ipa

def pcoda(syllable):
    bx = parse_baxter(syllable)
    if bx[-2][-1] == 'p':
        return True
    return False


def tcoda(syllable):
    bx = parse_baxter(syllable)
    if bx[-2][-1] == 't':
        return True
    return False


def qutone(syllable):
    bx = parse_baxter(syllable)
    if bx[-1] == 'H':
        return True
    return False


def sandeng(syllable):
    """Check if a syllable belongs to the third děng.
    """
    bx = parse_baxter(syllable)
    if 'j' in bx[1] or 'i' in bx[2]:
        return True
    return False


def velars(syllable):
    bx = parse_baxter(syllable)
    if bx[0] in ['k', 'kh', 'g', 'h', 'x']:
        return True
    return False


def glottals(syllable):
    bx = parse_baxter(syllable)
    if bx[0] in ['y', "'", "'y"]:
        return True
    return False


def lateral(syllable):
    bx = parse_baxter(syllable)
    if bx[0] in 'l':
        return True
    return False


