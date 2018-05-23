def anagram(s1, s2):
    a = sorted(list(s1.lower()))
    b = sorted(list(s2.lower()))
    if a == b:
        return True
    else:
        return False


print(anagram("nitin", "iyinn"))
