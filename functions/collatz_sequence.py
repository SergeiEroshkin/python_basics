def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print number
        else:
            number = 3 * number + 1
    return number


guess = int(raw_input('Please enter number: '))
print collatz(guess)