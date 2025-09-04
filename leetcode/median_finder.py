import heapq

# revisit 2 balanced heaps solution.

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    '''
    max_heap = [5 4 2 3]
    min_heap = [6 10 25 15]

    25 3 15 4 2 10 6

    2
    max_heap = [25]
    min_heap = [2]

    5
    max_heap = [10]
    min_heap = [5, 2]

    if adding the new element will make it the head of one of the 
    heaps and there for shorten the distance between the two heads, we need
    to add it to that heap.
    
    if elem > min_heap[0] and elem < max_heap[0]:
        heapq.heappush(min_heap, elem)
    if elem > max_heap[0]
    '''
    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append()
        # i, j = 0, len(self.stream)-1
        # lastGreaterIdx = 0
        # while i <= j:
        #     m = i+((j-i)//2)
        #     if self.stream[m] >= num:
        #         lastGreaterIdx=m
        #         j = m-1
        #     if self.stream[m] < num:
        #         lastGreaterIdx=m+1
        #         i = m+1
        # self.stream = self.stream[0:lastGreaterIdx] + [num] + self.stream[lastGreaterIdx:len(self.stream)]


    '''
    to find the median, we really only need to know middle element(s).
    can keep two heaps of the same size.
    max-heap
    min-heap

    if element greater than max_heap[0] then add to min_heap.
    if element smaller than min_heap[0] then add to max_heap.

    max_heap = [5 4 2 3]
    min_heap = [6 10 25 15]
    '''
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + self.max_heap[0]) / 2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return self.max_heap[0]
        # n = len(self.stream)
        # if n%2 == 1:
        #     return self.stream[(n-1)//2]
        # else:
        #     return (self.stream[(n-1)//2] + self.stream[(n)//2])/2