# insertion sort - O(n**2)
# good online algorithm - it can sort list as it receives new elements
import random


def insertion_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i

        while j > 0 and array[j - 1] > value:
            array[j] = array[j - 1]
            j = j - 1

        array[j] = value


if __name__ == "__main__":
    array = [random.randint(1, 20)]
    array_len = random.randint(10, 20)

    for i in range(1, array_len):
        array.append(random.randint(1, 20))

    print('Array before sorting: ', array)
    insertion_sort(array)
    print('Array after sorting: ', array)
