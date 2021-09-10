from itertools import permutations

strPerms = lambda string: permutations(string)

def charHasTwin(index, string):
    if index >= len(string) - 1:
        return False
    else:
        return string[index] == string[index + 1]

def strHasTwins(string):
    return any(charHasTwin(index, string) for index in range(len(string)))

def permAlone(string):
    permsHaveTwins = (strHasTwins(strPerm) for strPerm in strPerms(string))
    permsAlone = filter(lambda perm: not perm, permsHaveTwins)
    return len(list(permsAlone))
