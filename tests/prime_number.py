def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True