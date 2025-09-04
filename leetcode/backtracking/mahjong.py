
from collections import Counter
#import functools

# tiles = 11111
def validateWinningTiles(tiles: str):
    arr = [int(tile) for tile in list(tiles)]
    # {1->5}
    cts = Counter(arr)
    return isWinning(cts, 0, arr, False)

# we need a way to iterate through the keys
#@functools.cache
def isWinning(cts: dict, i: int, keys: list, foundPair: bool):
    if i >= len(keys):
        # base case
        # cts for all keys should be 0
        for key in cts.keys():
            if cts[key] > 0:
                return False
        return True

    # is current tile part of a triple, consecutive sequence, or pair
    tile = keys[i]

    '''
        /  \
       111 11
      /      \
     11111  11111
    '''
    res = False
    if (tile + 1) in cts and (tile + 2) in cts and cts[tile+1] > 0 and cts[tile+2] > 0:
        # dict.copy() creates a shallow copy, wont replicate nested objects
        copy = cts.copy()
        copy[tile] -= 1
        copy[tile+1] -= 1
        copy[tile+2] -= 1
        res |= isWinning(copy, i+1, keys, foundPair)
    if cts[tile] >= 3:
        copy = cts.copy()
        copy[tile] -= 3
        res |= isWinning(copy, i+1, keys, foundPair)
    if cts[tile] >= 2 and not foundPair:
        copy = cts.copy()
        copy[tile] -= 2
        res |= isWinning(copy, i+1, keys, True) 

    res |= isWinning(cts, i+1, keys, foundPair) 

    return res

print(validateWinningTiles("11123"))



