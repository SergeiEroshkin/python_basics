# Given infinite sequence : .....-1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0 ......
# Write function that will return Nth (case) element in sequence
# Example num1 = -1; num2 = -1; case = 1 element == 0


def get_element(num1, num2, case):
    for item in range(case):
        num1, num2 = num2, num2 - num1
    return num2


def main():
    for item in range(1, 7):
        print get_element(-1, -1, item)


if __name__ == '__main__':
    main()
