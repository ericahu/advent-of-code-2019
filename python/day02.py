def part01(code):
    i = 0
    while code[i] != 99:
        a = code[i+1]
        b = code[i+2]
        c = code[i+3]
        if code[i] == 1:
            code[c] = code[a] + code[b]
        elif code[i] == 2:
            code[c] = code[a] * code[b]
        i += 4
    return code

def part02(code, target=19690720):
    for noun in range(100):
        for verb in range(100):
            new_code = code.copy()
            new_code[1] = noun
            new_code[2] = verb
            new_code = part01(new_code)
            if new_code[0] == target:
                return 100 * noun + verb
