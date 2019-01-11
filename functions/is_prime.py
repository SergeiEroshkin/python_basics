def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            print '{0} is not prime number'.format(number)
            break
    else:
        print '%d is prime number' % number


print is_prime(13)
print is_prime(12)
