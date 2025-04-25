#
# j = input('trashers: ')
# s = input('stones & trashers: ')
# cnt = 0
# for i1 in s:
#     for i2 in j:
#         if i1 in i2:
#             cnt+=1
#
# print(f"match trashers and stones: {cnt}")
# answ = []
# candidates = [2,5,2,1,2]
# cnt = len(candidates)
# target = 5
# # print(candidates[::-1],'/n', candidates[:-1])
# for i in range(cnt):
#     if candidates[i] + candidates[i-1] == target:
#         print('y')
#         print(candidates[i])
#     else:
#         print('n')
# l=0
# target = int(input())
# while l == len(target):
#     l = [0*l]
#     print(l)


# if candidates[len(candidates)+1] + candidates[len(candidates)] == target :
#     print(answ.append(candidates[len(candidates)-1] ))

# arr=[]
# count = [1,2,3,4,5]
# for _ in range(len(count)):
#     for i in range(0,10):
#         # arr=[0 * 5]
#         arr.append(i)
#         print(i,arr)
# a = 0
# arr=[]
#
# count = [1,2,3,4,5]
# trigger = int(input())
# for _ in range(len(count)):
#     for i in range(10):
#         i+=1
#
#         arr.append(i)
#         print(i, arr)
# print(arr)
#

# t = 5
# g = sorted([2,5,2,1,2])
# def solution(g,t):
#     sum = 0
#     for i in g:
#         sum+=i
#         if i>=t or sum>t :
#             return 0
#             print(i)
#         else:
#             return 1
# print(solution(g,t))
# print(g)



import itertools

def unique_target_combinations(candidates, target):
    target_combinations = []
    for i in range(1, len(candidates) + 1):
        combinations = [sorted(list(combinaton)) for combinaton in itertools.combinations(candidates, i)]
        for combination in combinations:
            if sum(combination) == target and combination not in target_combinations:
                target_combinations.append(combination)
    return target_combinations

candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
print(unique_target_combinations(candidates, target)) 

