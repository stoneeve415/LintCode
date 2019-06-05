"""
@title: 13.字符窜查找
@author: evestone
"""


def next_arr(target):
    _len = len(target)
    arr = list(target)
    res = [0]*_len
    if _len == 1:
        return res
    for i, item in enumerate(arr[1:], start=1):
        if arr[i] == arr[res[i-1]]:
            res[i] = res[i-1] + 1
        else:
            res[i] = res[i-1]
    return res


def kmp(source, target):
    if target == '':
        return 0
    prefix = next_arr(target)
    prefix.insert(0, -1)
    i, j = 0, 0
    len1, len2 = len(source), len(target)
    while i < len1:
        if source[i] == target[j]:
            i += 1
            j += 1
            if j == len2:
                return i - j
        else:
            if j != -1:
                j = prefix[j]
            else:
                j += 1
                i += 1
    return -1


if __name__ == '__main__':
    source = 'tartarget'
    target = 'target'
    print(kmp(source, target))
