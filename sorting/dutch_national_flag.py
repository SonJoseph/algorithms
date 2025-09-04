'''
We keep three regions:

css
Copy
Edit
[0 ... lo-1]      → all 0’s (correct place)
[lo ... mid-1]    → all 1’s
[mid ... hi]      → unknown/unprocessed
[hi+1 ... end]    → all 2’s (correct place)
Step-by-step for arr[mid] == 0:
We know that mid is in the "unknown" section, and lo is the start of the "1’s" section.

Swapping arr[mid] with arr[lo] moves the 0 into the lo position — where all the 0’s go.

Before the swap, arr[lo] was either:

1 (normal case), or

the algorithm never allows it to be 0 or 2 here.

After the swap:

arr[lo] is 0 → correct section.

arr[mid] is the old arr[lo], which must be 1 → already belongs in the middle section.

Because of this guarantee, mid doesn’t need to reprocess its new element — it’s automatically in the right section.
'''
# def sort(arr: list[int]):
#     '''
#     DNF algorithm invariant: Memorize.

#     [0, lo-1] 0s
#     [lo, mid-1] 1s
#     [mid, hi] unknown *hi is inclusive. therefore mid <= hi. [2, 0, 1] case.
#     [hi+1, end]2s
#     '''
#     lo, mid, hi = 0, 0, len(arr) - 1

#     while mid <= hi:
#         if arr[mid] == 1:
#             mid += 1
#         elif arr[mid] == 0:
#             arr[lo], arr[mid] = arr[mid], arr[lo]
#             lo += 1 # lo now contains 0, so we can move up the boundary.
#             mid += 1 # mid must contain 1. [1, 0, 1], lo=0, mid=1, hi=2 or [0, 0, 2], lo=0, mid=0, hi= 2
#         else:
#             arr[hi], arr[mid] = arr[mid], arr[hi]
#             hi -= 1

'''
[0, lo-1]: 0s
[lo, mid-1]: 1s
[mid, hi]: unknown
[hi+1, end]: 2s

'''
def sort(arr: list[int]):
    lo, mid, hi = 0, 0, len(arr)-1

    while mid <= hi:
        if arr[mid] == 0:
            '''
            [1, 0, 2]
            '''
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[hi], arr[mid] = arr[mid], arr[hi]
            hi -= 1


arr = [2,0,2,1,1,0]
sort(arr)

# [0, 0, 1, 1, 2, 2]
print(arr)

