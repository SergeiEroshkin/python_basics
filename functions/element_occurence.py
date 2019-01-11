# Given infinite sequence : .....-1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0 ......
# Write function that will return Nth (case) element in sequence
# Example num1 = -1; num2 = -1; case = 1 element == 0


def get_element(num1, num2, case):
    # Amount of iterations defined by case
    for item in range(case):
        num1, num2 = num2, num2 - num1
    return num2


def main():
    elements_list = []
    for item in range(1, 7):
        elements_list.append(get_element(-1, -1, item))
    print elements_list
    print 'Seventh number is {0}'.format(get_element(-1, -1, 7))


if __name__ == '__main__':
    main()
