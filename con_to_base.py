DIGITS = '0123456789abcdef'


def con_to_base(dec_no, base):
    remainder_stack = []

    while dec_no > 0:
        remainder = dec_no % base
        remainder_stack.append(remainder)
        dec_no = dec_no // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)


print(con_to_base(25, 2))
print(con_to_base(25, 16))
