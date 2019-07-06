# -*- coding: utf-8 -*-
"""
@title: 最长无重复字符的子串
@author: evestone
"""


def lengthOfLongestSubstring(s):
    # write your code here
    _max = 0
    cnt = 0  # 统计当前长度
    n = len(s)
    mhash = {}  # 记录出现位置
    cur = 0  # 记录当前最左边位置
    for i in range(n):
        if s[i] not in mhash or mhash[s[i]] < cur:
            cnt += 1
            mhash[s[i]] = i
        else:
            if cnt > _max:
                _max = cnt
            cur = mhash[s[i]] + 1
            mhash[s[i]] = i
            cnt = i - cur + 1
    if cnt > _max:
        _max = cnt
    return _max


if __name__ == '__main__':
    s = 'bpfbhmipx'
    print(lengthOfLongestSubstring(s))