def prime(n):
    prime_list = list()
    # Let's walk through the list:
    for number in range(2, n+1):
        # Let's check if number in list is prime number
        for item in range(2, number):
            if number % item == 0:
                break
        else:
            prime_list.append(number)
    return prime_list


print prime(23)
print prime(46)

