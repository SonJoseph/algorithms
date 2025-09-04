'''
Given a set of known suspicious activites, return a list of suspicious activities found in new activities.

A new suspicious activity is defined as having atleast k of the same values as a "node" in suspicous activities.
A newly identified suspicipous activity can be used to identify other suspicious activities. (Hint : Recursion)

suspiciousactivities = [
("Brad", "San Francisco", "withdraw"),
]

newactivities = [
("Joe", "Miami", "withdraw"),
("John", "San Francisco", "deposit"),
("Albert", "London", "withdraw"),
("Diana", "London", "withdraw"),
("Diana", "San Francisco", "withdraw"),
("Joe", "New York", "updateaddress"),
]

k = 2;

findsuspiciousactivities(suspiciousactivites, newactivities, k) = [
("Albert", "London", "withdraw")
("Diana", "London", "withdraw"),
("Diana", "San Francisco", "withdraw")
]

Explanation : Initially ("Diana", "San Francisco", "withdraw") is identified as the suspicious activity list, this adds "Diana" to the suspicious activity set,
then ("Diana", "London", "withdraw") is also suspicious, which adds "London" to suspicious activity set now,
which now adds ("Albert", "London", "withdraw") in the final list.
'''

suspiciousactivities = [
("Brad", "San Francisco", "withdraw"),
]

newactivities = [
("Joe", "Miami", "withdraw"),
("John", "San Francisco", "deposit"),
("Albert", "London", "withdraw"),
("Diana", "London", "withdraw"),
("Diana", "San Francisco", "withdraw"),
("Joe", "New York", "updateaddress"),
]

'''
Actually we dont need to generate the permutations.
Assuming all activities are the same length m, we can just do set subtraction and 
if new_activity - suspicious_activity == m - k

And we also don't need to repeat search that match for old suspicious_activities
because no new suspicious activities will rely on those values (they were already found).

final_suspicious_activities = []

# this can be a queue of activities we can pop when done processing
while suspicious_activities:
    suspicious_activity = suspicious_activities.popleft()

    remove_activities = set()
    for i, new_activity in enumerate(new_activities):
        if new_activity - suspicious_activity == m - k:
            suspicious_activity.append(new_activity)
            # we can also remove this new_activity
            remove_activities.add(i)

    # so that we're not updating collection mid-iteration.
    new_activities = [new_activities[i] for i in new_activities if i not in remove_activites]

    final_suspicious_activities.append(curr)

return final_suspicious_activities
    


In the original list of suspicious activity nodes, create a set of 
all k permutation of activities that exist for each node.
So if k = 2,
 that is O(m choose k) where m is the total number of values for each node.
  ("Brad", "San Francisco"),
  ("San Francisco", "withdraw"),
  ("Brad", "withdraw")
If there is a new activity that contains all of these activities, then
it's a new suspicious activity which we need to generate permutations for.
This results in a another linear scan (O(n)) to determine if there are any new suspicious activities.
We do this until there are no new suspicious activities.

For sake of simplicity, let's assume each activity is a set.

suspicious_activity_permutation - new_activity = 0. 
'''
suspiciousactivities = [
("Brad", "San Francisco", "withdraw"),
]

newactivities = [
("Joe", "Miami", "withdraw"),
("John", "San Francisco", "deposit"),
("Albert", "London", "withdraw"),
("Diana", "London", "withdraw"),
("San Francisco", "withdraw"),
("Joe", "New York", "updateaddress"),
]

k = 2

from collections import deque

def findsuspiciousactivities(suspicious_activities: list, new_activities: list, k: int) -> list:
    # convert to sets 
    suspicious_activities = deque([set(s) for s in suspicious_activities])
    new_activities = [set(s) for s in new_activities]
    final_suspicious_activities = []

    # assume all activities are of the same length
    # m = len(suspicious_activities[0])

    # process all new suspicious_activities that can cause new_activities to be added
    while suspicious_activities:
        suspicious_activity = suspicious_activities.popleft()

        remaining_activities = []
        for new_activity in new_activities:
            '''
            set A & B gives you elements in common, can handle sets of different lengths.
             - Use this for finding overlaps between sets vs. set subtraction!

            {"Brad", "San Francisco", "withdraw"} & {"Diana", "San Francisco", "withdraw", "Seattle"}
            '''
            if len(new_activity & suspicious_activity) >= k:
                suspicious_activities.append(new_activity)
                # we can also remove this new_activity
            else:
                remaining_activities.append(new_activity)

        new_activities = remaining_activities

        # so that we're not updating collection mid-iteration.
        # can clean this up by creating  new list that contains the items we wont remove during the loop.
        #new_activities = [new_activities[i] for i in range(len(new_activities)) if i not in remove_activities]

        final_suspicious_activities.append(suspicious_activity)

    return final_suspicious_activities

print(findsuspiciousactivities(suspiciousactivities, newactivities, 2))
