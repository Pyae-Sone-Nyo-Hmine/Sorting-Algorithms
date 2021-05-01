def merge_sort(arr):
    
    # the function will execute until the array has at least 2 values to sort for recursion
    if len(arr) > 1:

        # divide the array into half
        midpoint = len(arr)//2

        left = arr[:midpoint]
        right = arr[midpoint:]

        # calling recursion over the left and right arrays
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        #checks which side of the arrays i/j value is bigger and put it in the arrays k position
        while i < len(left) and j < len(right):

            if left[i] <right[j]:
                arr[k] = left[i]
                i += 1
            
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # executes  any leftovers
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr
