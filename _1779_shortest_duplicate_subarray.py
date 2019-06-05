"""
@title: 1779,最短重复子数组
@author: evestone
"""


def getLength(arr):
    # Write your code here.
    hashMap = {}
    ans = -1
    for i in range(len(arr)):
        if hashMap.get(arr[i]) is None:
            hashMap[arr[i]] = i
        else:
            cur = i - hashMap[arr[i]] + 1
            if ans == -1:
                ans = cur
            else:
                ans = min(ans, cur)
            hashMap[arr[i]] = i
    return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 1, 4, 5, 4, 6, 8]
    print(getLength(arr))
