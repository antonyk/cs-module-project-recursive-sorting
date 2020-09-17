# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a, b = 0, 0

    for i in range(len(merged_arr)):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # guided version:
    # if len(arr) > 1:
    #     left = merge_sort(:len(arr) // 2)
    #     right = merge_sort(len(arr) // 2:)
    #     arr = merge(left, right)

    # return arr

    if len(arr) < 2:
        return arr

    # a potentially better way to split off  the array
    # leftArr = arr[::2]
    # rightArr = arr[1::2]

    # spawn sub arrays
    mid_idx = len(arr) // 2
    leftArr = merge_sort(arr[:mid_idx])
    rightArr = merge_sort(arr[mid_idx:])

    # process each sub-array
    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(leftArr) and right_idx < len(rightArr):
        if leftArr[left_idx] < rightArr[right_idx]:
            merged.append(leftArr[left_idx])
            left_idx += 1
        elif leftArr[left_idx] > rightArr[right_idx]:
            merged.append(rightArr[right_idx])
            right_idx += 1

    # append remainders
    merged += leftArr[left_idx:]
    merged += rightArr[right_idx:]

    return merged


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# Maryam implementation
def merge_sort_with_helper(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    return merge(merge_sort_with_helper(arr[::2]), merge_sort_with_helper(arr[1::2]))
