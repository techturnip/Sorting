# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements

    merged_arr = []

    # left iterator
    i = 0
    # right iterator
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            i += 1

        else:
            merged_arr.append(arrB[j])
            j += 1

    merged_arr += arrA[i:]
    merged_arr += arrB[j:]
    # TO-DO


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    print(merge(l, r))
    return merge(l, r)

merge_sort([10, 8, 6, 2, 1, 5, 7, 3])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
