def partition(start, end, arr): # O(n^2)
    # sets the pivot point and it's index
    pivot_index = start
    pivot = arr[pivot_index]

    # runs the loop while start index is less than end index
    while start < end:

        # increase start index if the start value is smaller than the pivot
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        # decreases end index if the end value is larger than the pivot
        while arr[end] > pivot:
            end -= 1
        # swaps the start and end by checking that start has not surpass end
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

        arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end


def quick_sort(start, end, arr):
    # function calls the quick sort recursively
    if start < end:
        p = partition(start, end, arr)

        # quick_sort left and right arrays of pivot
        quick_sort(start, p - 1, arr)
        quick_sort(p + 1, end, arr)

    return arr
