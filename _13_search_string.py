"""
@title: 13.字符窜查找
@author: evestone
"""


def kmp(source, target):
    # Write your code here
    def next_arr(target):
        n = len(target)
        prefix = [0] * n
        i = 1
        _len = 0
        while i < n:
            if target[i] == target[_len]:
                _len += 1
                prefix[i] = _len
                i += 1
            else:
                if _len > 0:
                    _len = prefix[_len - 1]
                else:
                    prefix[i] = 0
                    i += 1
        return prefix

    if target == '':
        return 0
    prefix = next_arr(target)
    prefix.insert(0, -1)
    i, j = 0, 0
    while i < len(source):
        if j == len(target) - 1 and source[i] == target[j]:
            return i - j
        if source[i] == target[j]:
            i += 1
            j += 1
        else:
            if j != -1:
                j = prefix[j]
            else:
                i += 1
                j += 1
    return -1


if __name__ == '__main__':
    source = 'tartarget'
    target = 'target'
    print(kmp(source, target))
