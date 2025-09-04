'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

tasks = ["A","A","A","B","B","B"], n = 2

keep a queue of size n, which mantains order of task scheduled.

prque = [(3, A), (3, B)]

prque.pop() = A

schedule = [A, ]

prque = [(2, A), (3, B)]

prque.pop() = B

schedule = [A, B]

prque = [(2, A), (2, B)]

prque.pop() = (2, A)

keep track of last n elements as a set?
last_n = [A, B]

if prque.pop() # distinct elements in A, B:
    then we need to idle?

schedule = [A, B, idle]

last_n.remove(schedule[-n])

schedule[-n] is the oldest element, we should add it to the schedule.
'''

from collections import heapq, defaultdict

def leastInterval(tasks, n):
    schedule = []
    task_ct = defaultdict(int)
    prque = []
    last_n = set()

    for task in tasks:
        task_ct[task] += 1

    for task, ct in task_ct.items():
        heapq.heappush(prque, (-1*ct, task))
    
    '''
    prque = (-1,A), (-2, B)
    schedule = [A, B, idle, A]
    last_n = {B, A}

    1.
    (-3, A)
    2.
    (-3, B)
    3.
    (-2, A)
    4.
    (-2, A)
    5. (-2, B)
    '''
    # We have to idle at least every n scheduled.
    # two tasks, 5 interval.
    # A, B, idle, idle, idle, A
    while prque:
        ct, task = heapq.heappop(prque)
        if task not in last_n:
            schedule.append(task)
            last_n.add(task) # <- NAH
            if ct+1 < 0:
                # still need to schedule these tasks.
                heapq.heappush(prque, (ct+1, task))
        else:
            if len(last_n) == n:
                # we can schedule this element next.
                # A, B, idle, 
                if schedule[-n] = "idle":
                last_n.remove(schedule[-n])
                schedule.append("idle")

                if ct+1 < 0:
                    # still need to schedule these tasks.
                    heapq.heappush(prque, (ct+1, task))
            else:
                # we can't schedule this task, so we should process other possible tasks that can be scheduled.
                heapq.heappush(prque, (ct, task)) # but this will result in infinite loop...
                continue 
    
    return schedule

print(lastInterval(["A","A","A","B","B","B"], 2))

