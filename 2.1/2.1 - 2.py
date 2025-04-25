import itertools
candidates = [5, 4, 3, 6, 3, 2]
target = 8
def combinations_of_target_value(candidates, target):
    comb_to_target = set()
    for i in range(1, len(candidates) + 1):
        combo = itertools.combinations(candidates, i)
        for combination in combo:
            if sum(combination) == target:
                comb_to_target.add(tuple(sorted(combination)))
    return  comb_to_target
print(combinations_of_target_value(candidates, target))
