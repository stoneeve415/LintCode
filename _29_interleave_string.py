"""
@title: 29, 交叉字符串
@author: evestone
"""

def interleave1(s1, s2, s3):
    """recursive to implement"""
    def recur(a1, a2, a3):
        l1, l2, l3 = len(a1), len(a2), len(a3)
        if l1+l2 != l3:
            return False
        if l1 != 0 and l2 != 0 and a1[0] == a2[0]:
            if a1[0] == a3[0]:
                return recur(a1[1:], a2, a3[1:]) or recur(a1, a2[1:], a3[1:])
        elif l1 != 0 and a1[0] == a3[0]:
            return recur(a1[1:], a2, a3[1:])
        elif l2 != 0 and a2[0] == a3[0]:
            return recur(a1, a2[1:], a3[1:])
        else:
            if l1 == 0 and l2 == 0:
                return True
            else:
                return False
    a1, a2, a3 = list(s1), list(s2), list(s3)
    return recur(a1, a2, a3)


def interleave2(s1, s2, s3):
    """dp to implement"""
    l1, l2, l3 = len(s1), len(s2), len(s3)
    if l1 + l2 != l3:
        return False
    dp = [[False]*(l2+1) for i in range(l1+1)]  # s1:i,s2:j can make up s3:i+j
    dp[0][0] = True
    for i in range(1, l1+1):
        dp[i][0] = s1[:i] == s3[:i]
    for j in range(1, l2+1):
        dp[0][j] = s2[:j] == s3[:j]
    for i in range(1, l1+1):
        for j in range(1, l2 + 1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

    return dp[l1][l2]


if __name__ == '__main__':
    s1 = ""
    s2 = "a"
    s3 = "a"
    print(interleave1(s1, s2, s3))
    print(interleave2(s1, s2, s3))
