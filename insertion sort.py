def insertion_sort(arr):  # O(n^2)

    # goes through the array
    for i in range(len(arr) - 1):

        if arr[i + 1] < arr[i]:
            j = 0
            # sends the smaller number one step before the larger number
            # iteratively until the left number is smaller than the right

            while arr[i + 1 - j] < arr[i - j]:
                larger = arr[i - j]
                smaller = arr[i + 1 - j]
                arr[i - j] = smaller
                arr[i + 1 - j] = larger
                j += 1

    return arr
