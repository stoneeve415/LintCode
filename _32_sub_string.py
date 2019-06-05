"""
@title: 32,最小子串覆盖
@author: evestone
"""


# # 最小子串覆盖
def min_windows(source, target):
    res = ""
    if len(source) < len(target):
        return res

    left = 0
    right = 0
    min_len = len(source) + 1
    m = {}
    count = 0
    for i in target:
        m[i] = m.get(i, 0) + 1  # 统计t中字符数目
    while right < len(source):
        if source[right] in m:
            m[source[right]] -= 1
            if m[source[right]] >= 0:
                count += 1
            while count == len(target):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = source[left:right + 1]
                if source[left] in m:
                    m[source[left]] += 1
                    if m[source[left]] > 0:
                        count -= 1
                left += 1
        right += 1
    return res

# # 查找全排列子串
def perm_string1(s1, s2):  # 会超时
    # write your code here
    arr = list(s1)
    temp = arr.copy()
    left, right = 0, 0
    while right < len(s2):
        while left < len(s2) and s2[left] not in temp:
            left += 1
        right = left
        if right >= len(s2):
            return False
        while right < len(s2) and s2[right] in temp:
            temp.remove(s2[right])
            right += 1
            if len(temp) == 0:
                return True
        left += 1
        right = left
        temp = arr.copy()

    return False


def perm_string2(s1, s2):
    # write your code here
    l1 = len(s1)
    need = {}
    for i in s1:
        need[i] = need.get(i, 0) + 1
    missing = l1
    for i, c in enumerate(s2):
        if c in need:
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
        if i >= l1 and s2[i - l1] in need:
            need[s2[i - l1]] += 1
            if need[s2[i - l1]] > 0:
                missing += 1
        if missing == 0:
            return True
    return False


# 字符串全排列 递归
def string_perm1(source):
    str = list(source)
    res = []

    def recursive(str, begin, end):
        if begin >= end-1:
            res.append(''.join(str))
        else:
            for i in range(begin, end):
                if i == begin or not str[i] in str[begin:i]:
                    str[i], str[begin] = str[begin], str[i]
                    recursive(str, begin+1, end)
                    str[i], str[begin] = str[begin], str[i]
    recursive(str, 0, len(str))
    return res


# 字符串全排列 非递归
def string_perm2(source):
    str = list(source)
    str.sort()
    res = []
    low, high = 0, 0
    res.append(''.join(str))
    while True:
        low = len(str)-1
        while low > 0 and str[low-1] >= str[low]:
            low -= 1
        high = low
        low -= 1
        if low < 0:
            break
        while high < len(str) and str[high] >= str[low]:
            high += 1
        high -= 1
        str[low], str[high] = str[high], str[low]
        str[low+1:] = reversed(str[low+1:])
        res.append(''.join(str))
    return res


if __name__ == '__main__':
    source = "ADOBECODEBANC"
    target = "ABC"
    # print(min_windows(source, target))

    s1 = "ab"
    s2 = "eidbaoo"
    # print(perm_string1(s1, s2))
    # print(perm_string2(s1, s2))

    source = "123"
    print(string_perm1(source))
    print(string_perm2(source))

