PAIRINGS = {'(': ')', '{': '}', '[': ']'}


def is_balanced(symbols):

    stack = []
    for s in symbols:
        if s in PAIRINGS.keys():
            stack.append(s)
        else:
            try:
                expected_open_symbol = stack.pop()
            except IndexError:
                return False
            if s != PAIRINGS[expected_open_symbol]:
                return False
    return len(stack) == 0


print(is_balanced('{{([][])}()}'))
print(is_balanced('{[])'))
print(is_balanced('((()))'))
print(is_balanced('(()'))
print(is_balanced('())'))
