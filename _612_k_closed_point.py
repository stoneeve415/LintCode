"""
@title: 612, k个最近的点
@author: evestone
"""

import heapq as hq


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def kClosest(points, origin, k):
        # write your code here
        length = len(points)
        if length == 0 or length < k:
            return -1
        heap = []
        res = []
        for i, item in enumerate(points):
            distance = (item.x-origin.x)**2 + (item.y-origin.y)**2
            element = (-distance, -item.x, -item.y)
            if i < k:
                hq.heappush(heap, element)
            else:
                if element > heap[0]:
                    hq.heapreplace(heap,element)
        while k>0:
            k -= 1
            element = hq.heappop(heap)
            res.append(Point(-element[1],-element[2]))
        res.reverse()
        return res


if __name__ == '__main__':
    points = [Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)]
    origin = Point(0, 0)
    k = 3
    print(kClosest(points, origin, k))
    