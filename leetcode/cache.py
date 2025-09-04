'''
say we have a series of requests of element x_i and a cache of max size n 
with m current elements in the cache.

if x_i is in the cache, then we don't evict an element from the cache.
if x_i is not in the cache:
    if m == n:
        We need to make room for it by evicting: "Least recently called".
        max(min(index element is present))

        If the last requested element is the element we're
        adding, then do nothing.
        Ex:
        case 1
        requestSeq = [a, a, b, c, a, c, b]
        cache = [a, b]
        i = 3, requestSeq[i] = c
        a is seen at index 4.
        c is seen at index 5.
        b is seen at index 6.
        so, remove b form the cache.
        
        case 2
        requestSeq = [a, a, b, c, a, b]
        cache = [a, b]
        i = 3, requestSeq[i] = c
        a is seen at index 4.
        b is seen at index 5.
        c, is not seen so don't add it to the cache.

        case 3
        requestSeq = [a, a, b, c, a, c, b, a]
        cache = [a, b]
        i = 3, requestSeq[i] = c
        a is seen at index 4 and 7.
        c is seen at index 5.
        b is seen at index 6.
        **we only care about the earliest access time for the element.
        - say we are at i=5, then we can pop indices off beginning of queue. 
          as we won't need to access these indices again during the forward iteration.

    else:
        Add it to the cache.

what i liked about this interview was we went through an example
of the expected result of the function.
i should be able to walkthrough an example and talk about what
the function would return and the logic of the algorithm based on 
the input.
i got confused when even explaining the expected input/output which
would definitely mean i cant implement the algorithm, so i should make sure
i can explain this first!
i got confused in explaining the logic out loud of deciding which
element to evict from the cache.
'''
from collections import deque 
from collections import defaultdict

def getEvicted(requests, cache_size):
    # need a dict of element -> indices. these are queues
    request_times = defaultdict(deque)

    for i in range(len(requests)):
        request_times[requests[i]].append(i)

    cache = set()
    evicted = []

    for i in range(len(requests)):
        print(f"Processing request {i}, element {requests[i]}")
        curr_req = requests[i]
        if curr_req in cache:
            pass
        else:
            if len(cache) < cache_size:
                cache.add(curr_req)
            else:
                '''
                case 3
                    requestSeq = [a, a, b, c, a, c, b, a]
                    cache = [a, b]
                    i = 3, requestSeq[i] = c
                    a is seen at index 4 and 7.
                    c is seen at index 5.
                    b is seen at index 6.
                '''
                candidates = cache.copy()
                candidates.add(curr_req)
                last_called = 0
                to_remove = ""
                for elem in candidates:
                    # only look at indices greater than the current one.
                    print(request_times[elem])
                    while(request_times[elem] and request_times[elem][0] <= i):
                        request_times[elem].popleft()
                    print(request_times[elem])
                    if not request_times[elem]:
                        # evict elem from the cache, in case of multiple cache elements
                        # not existing, we can just pick one to remove.
                        to_remove = elem
                        break
                    else:
                        print(f"Next occurence of element {elem}: {request_times[elem][0]}")
                        # remove "last next used"
                        if request_times[elem][-1] > last_called:
                            last_called = request_times[elem][0]
                            to_remove  = elem
                if to_remove == curr_req:
                    pass
                else:
                    cache.remove(to_remove)
                    cache.add(curr_req)
                    evicted.append(to_remove)

                print(f"Evicting {to_remove}")
    return evicted




