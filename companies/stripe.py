'''
given a string str and minor_parts
compress it so that for eachh part, major or minor 
(dileneated by / and . respectively), it is
[first letter][num characters][last letter]

e.g.
str = stripe.com/payments/checkout/custoemr.john.doe

s4e.c1m/p6s/.../c6r.j2n.d1e

Then, further compress so the last minor_part minor parts
are [frst letter][num characters][last letter]
'''

# sABCd -> s3d 
def compress_minor_part(s: str) -> str:
    return s[0] + str(len(s) - 2) + s[-1]

# s3d.f4d -> s9d
def merge(s1, s2) -> str:
    merged = s1 + s2
    ct = 0
    for c in merged[1:-1]:
        if str.isdigit(c):
            ct += int(c)
        else:
            ct += 1
    return s1[0] + str(ct) + s2[-1]
        

# threshold is the max number of minor parts before the last start to get compressed
def compress(s: str, threshold: int = 0) -> str:

    res = ""

    # stripe.com/payments -> ["stripe.com", "payments"]
    for major in s.split('/'):
        minor_parts = []

        for minor in major.split('.'):
            # stripe.com -> [s4e, c1m]
            minor_parts.append(compress_minor_part(minor))

            # len(minor_parts) == 1, nothing to merge it into
            if len(minor_parts) > threshold and len(minor_parts) > 1:
                overflow = minor_parts.pop()
                minor_parts[-1] = merge(minor_parts[-1], overflow)

        res += '.'.join(minor_parts) + "/"

    return res[:-1] # remove the trailing backslash

print(compress("stripe.com/payments/checkout/custoemr.john.doe", 0))
#print(part2compress("c6r.j2n.d1e", 2))

'''
what did i learn?

testing small pieces is helpful to iteratively build solution. 

python array slicing makes this problem way easier!

to get the last x elements of a list l, it is l[-x:]
to get all elements except the last x, it is l[:-x]
'''



'''

Given an inputString: "US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7" (etc) find the cost to ship an item from X to Y (ie: US to UK ==> Cost of 5).
From the previous solution, with the same inputString find the cost if you need to use an intermediate step. For instance US -> CA -> UK and it's associated cost.

'''
import heapq
from collections import defaultdict

def cheapest_cost(s: str, src: str, dst: str, threshold: int):
    '''
    s is formatted like so:
        source, dest, delivery service, cost

    create graph from s[0] to s[1] with cost s[3]  # s[2] can be ignored
        - directed graph so no need to add backedge

    can there be cycles?
        for example, us -> uk -> ca -> us

    let's do cheapest cost, so cycles wont be part of the solution.

    djikstra's approach.
     - keep cost array, cost from x to all other y
     - keep priority queue to process nodes shortest distance from source first.
        - prque = heapq

     - if cost[prque.pop().node] < prque.pop().cost then continue.
     - only enque if nei.cost + curr.cost < cost[nei], as this means this may be a shorter path. 

    then return, cost[dst]
    '''

    graph = defaultdict(list)
    cost = {}

    for edge in s.split(':'):
        info = edge.split(',')
        graph[info[0]].append((info[1], int(info[3])))

        # need to add both in case there is a node with no outedges
        cost[info[0]], cost[info[1]] = float('inf'), float('inf')

    cost[src] = 0
    
    prque = [(0, src, 0)]

    while prque:
        curr_cost, curr_node, curr_stops = heapq.heappop(prque)

        # deque: if a longer path was dequed, skip it. it's from a stale iteration of bfs.
        # the cost dictionary mantains the current state of shortest paths.

        # enque: shorter path was found
        if curr_cost > cost[curr_node]:
           continue

        for nei, nei_cost in graph[curr_node]:
            # only consider paths to the destination which has the [threshold] number of intermediate stops
            if nei == dst:
                if curr_stops < threshold:
                    continue

            if nei_cost + curr_cost < cost[nei]:
                heapq.heappush(prque, (nei_cost + curr_cost, nei, curr_stops + 1))
                cost[nei] = nei_cost + curr_cost

    return cost[dst]

print(cheapest_cost("US,UK,UPS,5:US,CA,FedEx,3:CA,UK,DHL,7", "US", "UK", 1)) # should return 8

'''
US - 5 ->  UK
           /
 \        2
  1 - CA /


US - 5 -> UK
     \    /
      \
       10
'''

'''
1. Mask Credit Card Numbers in Logs

Prompt:
You’re given logs with payment card numbers. You need to mask all digits except the last 4 of each card number.

def mask_card_numbers(log: str) -> str:
    """
    Mask all but the last 4 digits of any credit card numbers in the input log.
    A card number is assumed to be a sequence of 13 to 19 digits.
    """
    pass


Follow-ups:

Handle malformed numbers

Format the masked string consistently (e.g., **** **** **** 1234)
'''

def mask_card_numbers(log: str) -> str:
    parts = log.split(" ")
    if len(parts) != 4:
        raise RuntimeError("credit card number should contain only 4 parts")
    for i, part in enumerate(parts):
        if not str.isdigit(part):
            raise RuntimeError("credit card number should only contain digits")
        if len(part) != 4:
            raise RuntimeError("each part of the credit card number should contain 4 digits")
        if i != (len(parts)-1):
            parts[i] = "****"
    return " ".join(parts)

print(mask_card_numbers("1234 1234 1234 1234")) # **** **** **** 1234
#print(mask_card_numbers("12345 1234 1234 1234")) # throw error
#print(mask_card_numbers("12341234 1234 1234")) # throw error
#print(mask_card_numbers("1234 123a 1234 1234")) # throw error

'''
Given a nested dictionary and a list of keys, extract the value at that path.

def get_nested_value(data: dict, path: list) -> Any:
    """
    Traverse a nested dictionary and return the value at the specified path.
    
    Example:
    get_nested_value({"a": {"b": {"c": 3}}}, ["a", "b", "c"]) -> 3
    """
    pass


Follow-ups:

Raise a custom error if key is missing

Add default return value

Handle lists inside dicts
'''


def get_nested_value(data: dict, path: list):
    """
    Traverse a nested dictionary and return the value at the specified path.
    
    Example:
    get_nested_value({"a": {"b": {"c": 3}}}, ["a", "b", "c"]) -> 3

    data = {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ]
    }
    path = ["users", 1, "name"]
    """
    curr = data
    for level, key in enumerate(path):
        print(type(curr))
        if type(curr) is list:
            # get property of json objects in list
            for item in curr:
                # hardcoded to the above use-case without generalization.
                # always assumes when the current level is a list, we look for an item
                # with these fields and values in the path in this order.
                if item["id"] == key and item["name"] == path[level+1]:
                    return item
                
        if key not in curr:
            raise RuntimeError("key in path not found")
        curr = curr[key]

        if level == len(path)-1:
            return curr

print(
    get_nested_value({
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ]
    }, ["users", 2, "Bob"])
    )

'''
5. Rate Limit Log Entries

Prompt:
Simulate a rate-limiter for a logging system: only allow a message to be printed if it hasn't been printed in the last 10 seconds.

class Logger:
    def __init__(self):
        pass

    def should_print_message(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed at the given timestamp,
        otherwise returns false.
        """
        pass


This is a real Stripe interview question, adapted for clarity.

print(logger.should_print_message(1, "foo"))   # ✅ True — first time for "foo"
print(logger.should_print_message(2, "bar"))   # ✅ True — first time for "bar"
print(logger.should_print_message(3, "foo"))   # ❌ False — "foo" was printed at t=1 (<10s ago)
print(logger.should_print_message(8, "bar"))   # ❌ False — "bar" printed at t=2 (<10s ago)
print(logger.should_print_message(11, "foo"))  # ✅ True — now 10s after first "foo"
'''

'''
Need to keep a dictionary of the message and the last timestamp
that it was submitted. 
10 seconds must have passed from the current timestamp and that last timestamp
in order for it to be emitted. 
'''

class Logger:
    def __init__(self):
        self.messages = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed at the given timestamp,
        otherwise returns false.
        """
        # timestamp + 10 is the rate limit window. [1, 11)
        if message in self.messages and self.messages[message] + 10 > timestamp:
            # do not emit. 
            return False
        else:
            self.messages[message] = timestamp
            return True

logger = Logger()

print(logger.should_print_message(1, "foo")) # true
print(logger.should_print_message(5, "bar")) # true
print(logger.should_print_message(11, "foo")) # true
print(logger.should_print_message(11, "bar")) # false
