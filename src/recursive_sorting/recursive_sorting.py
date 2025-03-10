# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO

    while len(arrA) and len(arrB):
        if(arrA[0] <= arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    return [*merged_arr, *arrA, *arrB]


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr
    midPoint = len(arr) // 2
    arr1 = merge_sort(arr[:midPoint])
    arr2 = merge_sort(arr[midPoint:])
    
    return merge(arr1, arr2)


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
