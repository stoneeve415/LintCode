# -*- coding: utf-8 -*-
"""
@title: 最长不含重复字符的子字符串
@author: evestone
"""

def longestSubstring(s):
    mhash = {}
    _max = 0
    cur = 0
    i = 0
    while i < len(s):
        if s[i] not in mhash or mhash[s[i]] < cur:
            mhash[s[i]] = i
        else:
            if i - cur > _max:
                _max = i - cur
            cur = mhash[s[i]] + 1
            mhash[s[i]] = i
        i += 1
    if i - cur > _max:
        _max = i - cur
    return _max


if __name__ == '__main__':
    str = "arabcacfr"
    s = "abcabcbb"
    print(longestSubstring(s))