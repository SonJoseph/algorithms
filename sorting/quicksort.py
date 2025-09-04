'''
Start with pivot is the last index.
Keep two pointers:
i = item less than pivot
 - initialized to 0
j = item greater than pivot.
 - initialized to pivot index - 1.

while i < j:
    while arr[i] < pivot:
        i+=1
    while arr[j] > pivot:
        j-=1
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]

arr[j], arr[pivot_index] = pivot, arr[j]    
'''

'''
1 9 2 5 8
1 5 2 9 8
1 5 2 8 9
'''

# def sort(A: list[int]) -> None:
#     quicksort(A, 0, len(A)-1)

# '''
# [1, 2]
# pivot_index = 1
# '''
# def quicksort(A: list[int], lo: int, hi: int) -> None:
#     print(A)
#     if hi <= lo:
#         return
#     pivot_index = partition(A, lo, hi)
#     quicksort(A, lo, pivot_index - 1)
#     quicksort(A, pivot_index + 1, hi)


# '''
# Swap elements such that elements from lo to pivot-1 are less than the pivot
# and elements from pivot to hi are greater than the pivot.
# '''
# def partition(arr: list[int], lo: int, hi: int) -> None:
#     pivot = arr[hi]

#     i, j = lo, hi - 1

#     while True:
#         # increase i until it is greater than the pivot.
#         while i <= j and arr[i] < pivot:
#             i+=1
#         # decrease j until it is less than the pivot.
#         while i <= j and arr[j] > pivot:
#             j-=1
#         if i >= j:
#             break

#         arr[i], arr[j] = arr[j], arr[i]

#         i += 1
#         j -= 1

#     arr[i], arr[hi] = arr[hi], arr[i]

#     return i

'''
[3, 1]

[1, 3]
'''


def sort(arr: list[int]):
    quickSort(arr, 0, len(arr)-1)

def quickSort(arr: list[int], lo: int, hi: int):
    if hi <= lo:
        return 
    new_pivot = pivot(arr, lo, hi)
    quickSort(arr, lo, new_pivot-1)
    quickSort(arr, new_pivot+1, hi)


def pivot(arr: list[int], lo: int, hi: int):

    pivot_index = hi
    lessThan = lo
    gtThan = pivot_index - 1

    while True:
        # iterate the lessThan index until it finds an element greater than the pivot
        while lessThan <= gtThan and arr[lessThan] < arr[pivot_index]:
            lessThan += 1   
        
        while gtThan >= lessThan and arr[gtThan] > arr[pivot_index]:
            gtThan -= 1   

        if gtThan <= lessThan:
            break

        arr[lessThan], arr[gtThan] = arr[gtThan], arr[lessThan]

        lessThan += 1
        gtThan -= 1

    arr[lessThan], arr[pivot_index] = arr[pivot_index], arr[lessThan]

    return lessThan



A = [1, 9, 2, 5, 8]


sort(A)
# [1 2 5 8 9]
print(A)





