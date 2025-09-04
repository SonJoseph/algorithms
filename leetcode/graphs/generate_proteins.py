from collections import defaultdict
import functools

sequences = [
    ('acG', 0, 5),
    ('Bf5', 0, 22),
    ('e5c', 5, 16),
    ('6a5d', 5, 17),
    ('7f6c', 2, 13),
    ('0Pf', 13, 23),
    ('0f5c', 0, 13),
    ('xx', 16, 5)
]

start_at = defaultdict(list)

'''
0: [(acG, 0, 5), (Bf5, 0, 22)]
'''
for s in sequences:
    # could append the entire tuple.
    start_at[s[1]].append(s)

protein_graph = defaultdict(list)

'''
'acG' -> [('e5c', 5, 16), ('6a5d', 5, 17)]
'''
for s in sequences:
    protein_graph[s[0]] = start_at[s[2]]

all_seq = []

visited = set()

# For this protein, return all possible sequences.
@functools.cache
def dfs(protein):
    name, start, end = protein

    if name in visited:
        return []

    res = [(name, start, end)]

    visited.add(name)

    for neighbor in protein_graph[name]:
        # [('e5c', 5, 16), ('e5c_b12', 5, 25)]
        partial = dfs(neighbor)
        for p in partial:
            res.append((f"{name}_{p[0]}", start, p[2]))

    visited.remove(name)

    return res

for s in sequences:
    all_seq += dfs(s)

print(all_seq)
