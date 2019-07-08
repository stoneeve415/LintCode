# -*- coding: utf-8 -*-
"""
@title: 945. 任务计划
@author: evestone
"""


def leastInterval(tasks, n):
    # write your code here
    _len = len(tasks)
    mhash = {}
    for i in range(_len):
        if tasks[i] in mhash:
            mhash[tasks[i]] += 1
        else:
            mhash[tasks[i]] = 1
    max_key = max(mhash, key=mhash.get)
    max_value = mhash[max_key]

    ans = (max_value - 1) * (n + 1)
    for key, value in mhash.items():
        if mhash[key] == max_value:
            ans += 1
    return max(_len, ans)


if __name__ == '__main__':
    task = 'AAABBB'
    n = 2
    print(leastInterval(task, n))