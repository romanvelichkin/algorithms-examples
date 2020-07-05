# bubble sort - O(n**2)
import random


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def bubble_sort(array):
    for i in range(len(array) - 1):

        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


if __name__ == '__main__':
    array = [random.randint(1, 20)]
    array_len = random.randint(10, 20)

    for i in range(array_len):
        array.append(random.randint(1, 20))

    print('Array before sorting: ', array)
    bubble_sort(array)
    print('Array after sorting: ', array)


