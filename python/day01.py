def part01(mass):
    fuel = sum([int(m)//3-2 for m in mass])
    return fuel

def part02(mass):
    total_fuel = 0
    for m in mass:
        additional_fuel = int(m)//3-2
        while additional_fuel > 0:
            total_fuel += additional_fuel
            additional_fuel = additional_fuel//3-2
    return total_fuel
