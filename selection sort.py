# selection sort -  O(n**2)
# good if you need to do less memory writes
import random


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def selection_sort(array):
    for i in range(len(array) - 1):
        min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j

        swap(array, min, i)


if __name__ == '__main__':
    array = [random.randint(1, 20)]
    array_len = random.randint(10, 20)

    for i in range(1, array_len):
        array.append(random.randint(1, 20))

    print('Array before sorting: ', array)
    selection_sort(array)
    print('Array after sorting: ', array)
