def binary_search(my_list, item):
    # Set min and Max boundaries
    low = my_list[0]
    high = my_list[-1]
    # Execute this block until low became equal to high
    while low <= high:
        mid = (high + low) / 2
        if mid == item:
            return my_list.index(mid)
        if mid > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def main():
    my_list = range(101)
    number = 67
    print 'Positive Test:', binary_search(my_list, number)
    print 'None Test:', binary_search(my_list, 101)


if __name__ == '__main__':
    main()