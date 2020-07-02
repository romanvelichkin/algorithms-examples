# binary search - O(log(n, 2))
import random


def binary_search(array, search_value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if search_value == array[mid]:
            return mid

        elif search_value < array[mid]:
            right = mid - 1

        elif search_value > array[mid]:
            left = mid + 1

    return -1


if __name__ == "__main__":
    array = [random.randint(1, 10)]
    array_len = random.randint(10, 100)

    for i in range(1, array_len):
        random_val = array[-1] + random.randint(1, 10)
        array.append(random_val)

    print(array)
    print('Enter what value you want to find in this array:')
    search_value = int(input())

    result = binary_search(array, search_value)
    if result == -1:
        print('Value wasn\'t found in this array')
    else:
        print('Value was found in this array on position', result)
