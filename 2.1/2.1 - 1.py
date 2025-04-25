J = "ab"
S = "aabbccd"
def count_values(S, J):
    cnt = 0
    for i in range(len(J)):
        cnt += S.count(J[i])
    return cnt
print(count_values(S, J))
