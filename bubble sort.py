def bubble_sort(arr):  # O(n^2)

    n = len(arr)  # number of times to iterate through

    for i in range(n):  # execute bubble sort n times

        for j in range(1, n - i):

            if arr[j - 1] > arr[j]:  # swap if the first array is larger than the second
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr
