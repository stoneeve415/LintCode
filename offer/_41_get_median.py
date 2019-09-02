# -*- coding: utf-8 -*-
"""
@title: 数据流中的中位数
@author: evestone
"""

import heapq as hq

def getMedian(arr):
    _len = len(arr)
    # 最小堆
    heap1 = []
    # 最大堆
    heap2 = []
    for i in range(_len):
        if i & 1 == 0:
            hq.heappush(heap2, -arr[i])
        else:
            if arr[i] > -heap2[0]:
                hq.heappush(heap1, arr[i])
            else:
                hq.heappush(heap1, -heap2[0])
                hq.heapreplace(heap2, -arr[i])
    if _len & 1 == 0:
        return (heap1[0] - heap2[0]) / 2
    else:
        return -heap2[0]


if __name__ == '__main__':
    arr = [4, 5, 1, 6, 2, 7, 3, 8, 1, 1]
    print(getMedian(arr))
