# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    merged = []

    # Your code here

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

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

