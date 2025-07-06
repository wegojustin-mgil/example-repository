def calc_sum(a,b):
    return a+b

def calc_sub(a,b):
    return a-b

def calc_mul(a,b):
    return a*b

def calc_div(a,b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a/b

