from math import pi

def get_pi_decimal (num):

    if num > 16:
        return "Can't generate more than 16 decimal points"
    return f"{pi:.{num}f}"

print(get_pi_decimal(16))

