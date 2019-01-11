def find_smallest(lst):
    # Store smallest value
    smallest = lst[0]
    # Store smallest index
    smallest_idx = 0
    for index in range(1, len(lst)):
        if lst[index] < smallest:
            smallest = lst[index]
            smallest_idx = index
    return smallest_idx


def get_sorted(lst):
    sorted_list = []
    for item in range(len(lst)):
        smallest = find_smallest(lst)
        sorted_list.append(lst.pop(smallest))
    return sorted_list


a = [9, 90, 100, 1, 3, 2, 7]
print find_smallest(a)
print get_sorted(a)

