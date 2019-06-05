"""
@title: 78. 最长公共前缀
@author: evestone
"""



def longestCommonPrefix(strs):
    # write your code here
    res = []
    _len = len(strs)
    cur, short = 0, min([len(i) for i in strs])
    while cur < short:
        for i in range(1, _len):
            if strs[i][cur] != strs[i - 1][cur]:
                return strs[i][:cur]
        cur += 1
    return strs[0][:cur]


if __name__ == '__main__':
    strs = ["abc", "abcd", "", "ab", "ac"]
    print(longestCommonPrefix(strs))
