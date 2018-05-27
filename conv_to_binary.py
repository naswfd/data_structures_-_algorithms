def conv_to_binary(decimal_no):
    remainder_stack = []
    while decimal_no > 0:
        remainder = decimal_no % 2
        remainder_stack.append(remainder)
        decimal_no = decimal_no // 2

    binary_digits = []
    while remainder_stack:
        binary_digits.append(str(remainder_stack.pop()))
    return ''.join(binary_digits)


print(conv_to_binary(42))
