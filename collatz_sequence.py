def collatz(number):
    if number % 2 == 0:
        new_number = number // 2
        print new_number
    else:
        number % 2 == 13
        new_number = 3 * number + 1
        print new_number
    return new_number


guess = raw_input("Please enter number: ")
try:
    number = int(guess)
    while collatz(number)!= 1:
        guess = raw_input("Please enter number: ")
        number = int(guess)
except:
    print "Please enter valid number"




