# merge sort - O(n * log(n, 2))
#
import random


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        print('array after separating, left:', left, ', right:', right)
        left = merge_sort(left)
        right = merge_sort(right)

        print('  after recursion stop we have, left:', left, ', right:', right)

        sorted_array = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                sorted_array.append(left.pop(0))
                print('    after popping one element, left:', left)
                print('    after popping one element, left, sorted array:', sorted_array)
            else:
                sorted_array.append(right.pop(0))
                print('    after popping one element, right:', right)
                print('    after popping one element, right, sorted array:', sorted_array)


        for i in left:
            sorted_array.append(i)
            print('      after adding from left element to sorted array:', sorted_array)
        for i in right:
            sorted_array.append(i)
            print('      after adding from right element sorted array:', sorted_array)

        print()

    else:
        sorted_array = array

    return sorted_array


if __name__ == '__main__':
    array = []
    array_len = random.randint(5, 6)

    for i in range(array_len):
        array.append(random.randint(1, 10))

    print(array)
    sorted_array = merge_sort(array)
    print('array before sorting:', array)
    print('array after sorting:', sorted_array)

