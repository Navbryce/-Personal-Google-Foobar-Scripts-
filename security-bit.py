def answer(start, length):
    row_xors = set()
    cut_off_counter = 0
    row_start = start
    while cut_off_counter != length:
        value = XOR_range(row_start, row_start + length - 1 - cut_off_counter)  # -1 because row_start is already included
        if value in row_xors:
            row_xors.remove(value)  # two of the same value cancel out
        else:
            row_xors.add(value)
        cut_off_counter += 1
        row_start += length
    result = 0
    for value in row_xors:
        result ^= value
    return result


def XOR_range(lower_value, upper_value):
    return XOR_up_to_number(lower_value - 1) ^ XOR_up_to_number(upper_value)


def XOR_up_to_number(number):
    """XORS all numbers between 0 and that number
    including 0 and the number"""
    r = number % 4
    xor = None
    if r is 0:
        xor = number
    elif r is 1:
        xor = 1
    elif r is 2:
        xor = number + 1
    else:
        xor = 0
    return xor


def tests():
    assert(answer(0, 3) == 2)
    assert(answer(17, 4) == 14)
