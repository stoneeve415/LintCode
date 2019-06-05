"""
@title: 46 47 48, 主元素
@author: evestone
"""

def major1(nums):
    _len = len(nums)
    mhash = {}
    for i in nums:
        if i in mhash:
            mhash[i] += 1
        else:
            mhash[i] = 1
        if mhash[i] > _len / 2:
            return i
    return -1


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 2, 2, 2]
    print(major1(nums))
