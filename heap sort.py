def heapify(arr, n, i):  # O(nlgn)
    # set the largest value as index initially
    largest = i

    l = 2 * i + 1  # left children
    r = 2 * i + 2  # right children

    # set left largest if so
    if l < n and arr[largest] < arr[l]:
        largest = l
    # set right largest if so
    if r < n and arr[largest] < arr[r]:
        largest = r
    # switch if largest is not the initial index
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursion
        heapify(arr, n, largest)


def heap_sort(arr):
    # goes up the tree ( i gets smaller) and swap
    # we do len(arr)//2 b/c a number has two children
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

    # remove the largest element to be put in the end of the array
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
