# sum = 0
# a = int(input())
# while a > 0:
#     sum += a%10
#     a = a//10
# print(sum)

# import random
# arr = []
# a = int(input())
# c = int(input())
# for _ in range(10):
#     b = random.randrange(a,c)
#     arr.append(b)
# print(arr)

# import random
# arr = [0]*10
# for i in range(len(arr)):
#     arr[i] = random.randint(-100, 100)
#
# def opredel():
#     nul = 0
#     pol = 0
#     otr = 0
#
#     for i in range(len(arr)):
#         if arr[i]==0:
#             nul+=1
#         elif arr[i]>0:
#             pol+=1
#         else:
#             otr+=1
#     print(nul,pol,otr)
# opredel()
# print(arr)

import random
# for _ in range(10):
#     arr = [random.randint(1,10)]
# print(arr)
def minn(arr):
    diff = []
    for a in arr:
        print(a)

arr = [[[[random.randint(-10,10)]for a in range(2)]for b in range(2)]for c in range(2)]
print(minn(arr))
print(arr)