def prime(n):
    prime_list = list()
    for number in range(2, n+1):
        for item in range(2, number):
            if number % item == 0:
                break
        else:
            prime_list.append(number)
    return prime_list


print prime(23)
