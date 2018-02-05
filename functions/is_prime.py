def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            print '%d is not prime number' % number
            break
    else:
        print '%d is prime number' % number


print is_prime(13)
