# merge sort - O(n * log(n, 2))
#
import random


def merge_sort(array):

    if len(array) > 1:
        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]
        print('after separating array we have parts left:', left, 'and right:', right)
        left = merge_sort(left)
        right = merge_sort(right)

        print('when recursion stops we have parts left:', left, 'and right:', right)

        sorted_array = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))
            print('adding least element to sorted array:', sorted_array)

        print('after adding one element we have parts left:', left, 'and right:', right)

        for i in left:
            sorted_array.append(i)
        for i in right:
            sorted_array.append(i)

        print('add rest to sorted array:', sorted_array)
        print()

    else:
        sorted_array = array

    return sorted_array


if __name__ == '__main__':
    array = [random.randint(1, 20)]
    array_len = random.randint(10, 20)

    for i in range(1, array_len):
        array.append(random.randint(1, 20))

    array = [4, 3, 2, 1]

    print('Array before sorting: ', array)
    print()
    result = merge_sort(array)
    print('Array after sorting: ', result)
