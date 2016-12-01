prime_list = list()


def prime(n):
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    return prime_list
print prime(19)
