from collections import Counter

def part01(lower, upper):
    valid_count = 0
    for num in range(lower, upper):
        if _check_validity_basic(num):
            valid_count += 1
    return valid_count

def part02(lower, upper):
    valid_count = 0
    for num in range(lower, upper):
        if _check_validity_advanced(num):
            valid_count += 1
    return valid_count

def _check_validity_basic(num):
    repeated = False
    for i in range(len(str(num))-1):
        if str(num)[i] > str(num)[i+1]:
            return False
        if str(num)[i] == str(num)[i+1]:
            repeated = True
    return repeated

def _check_validity_advanced(num):
    for i in range(len(str(num))-1):
        if str(num)[i] > str(num)[i+1]:
            return False
    return 2 in Counter(str(num)).values()
