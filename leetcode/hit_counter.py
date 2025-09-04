'''
Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
 

Example 1:

Input
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output
[null, null, null, null, 3, null, 4, 3]

timestamps = [1, 2, 5]

Explanation
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
    hit[1] += 1
    if last_hit = -1:
        sums[1] = 1
    timestamps.append(ts)
hitCounter.hit(2);       // hit at timestamp 2.
     hits[2] += 1
     sums[2] = hits[2]+sums[timestamps[-1]] # sums stores a prefix sum.
     timestamps.append(ts)
hitCounter.hit(5);       // hit at timestamp 3.
    hits[5] += 5
    sums[5] = hits[5]+sums[timestamps[-1]]
    timestamps.append(ts)
hitCounter.getHits(6);   // get hits at timestamp 4, return 3.
    get the last timestamp which is > getHitTimestamp-300
     O(n) into timestamps or binary search.
     NO, we can pop element off queue! since timestamps we recieve
     are always increasing, we'll never need the earlier timestamps we pop.
    sums[timestamps[-1]] - sums[timestamps[0]]
hitCounter.hit(300);     // hit at timestamp 300.
    timestamps = [1, 2, 5]
    sums[300] = hits[300]+sums[timestamps[-1]]
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.
{
    1: 1,
    2: 1
    3: 1
    300: 1
    301: 1
}
def getHits(time):
    get all hits from [max(0, time-300+1), time]
        iterate through all keys, add to total numboer of hits if between this range.
        O(timestamps)
        insetad of searching through all timestamps, is there a way to quickly access
        the number of hits accumulated up until time?
        because timestamps are increasing, lets keep track of the last hit. 
'''

from collections import deque, defaultdict

class HitCounter:

    def __init__(self):
        self.timestamps = deque([])
        #self.hits = defaultdict(int) # since timestamp can have multiple hits. or can we just keep track of sums, hmm.
        self.sums = defaultdict(int)
        
    '''
    hitCounter.hit(1);       // hit at timestamp 1.
    hit[1] += 1
    if last_hit = -1:
        sums[1] = 1
    timestamps.append(ts)

    hitCounter.hit(2);       // hit at timestamp 2.
     hits[2] += 1
     sums[2] = hits[2]+sums[timestamps[-1]] # sums stores a prefix sum.
     timestamps.append(ts)
     '''
    def hit(self, timestamp: int) -> None:
        if not self.timestamps:
            self.sums[timestamp] = 1
        else:
            if timestamp not in self.sums:
                self.sums[timestamp] = self.sums[self.timestamps[-1]] + 1
            else:
                self.sums[timestamp] += 1
        self.timestamps.append(timestamp)

    '''
    hitCounter.getHits(6);   // get hits at timestamp 4, return 3.
    get the last timestamp which is > getHitTimestamp-300
     O(n) into timestamps or binary search.
     NO, we can pop element off queue! since timestamps we recieve
     are always increasing, we'll never need the earlier timestamps we pop.
    sums[timestamps[-1]] - sums[timestamps[0]]
    '''
    def getHits(self, timestamp: int) -> int:
        # [1:1, 5:2, 7:3, 301]
        too_old = 0
        while self.timestamps and self.timestamps[0] <= timestamp - 300:
            too_old = self.sums[self.timestamps.popleft()]

        if not self.timestamps:
            # no timestamps within (timestamp-300, timestamp]
            return 0

        # this returns the result: sum of timestamps from [0, timestamp] - sum of timestamps from [0, timestamp-300]
        return self.sums[self.timestamps[-1]] - too_old


hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
hc.hit(3)
hc.hit(5)

print(hc.getHits(304)) # should only return 1