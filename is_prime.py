def is_prime(value):
    if value <= 1:
        return True
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True
