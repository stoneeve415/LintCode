import sys

"""
@title: 41 42 43. 最大子数组
@author: evestone
"""


def maxSubArray(nums):
        # write your code here
        if len(nums) == 0:
            return 0
        sums = 0
        max_sum = -sys.maxsize - 1
        for item in nums:
            sums += item
            max_sum = max(sums, max_sum)
            sums = max(0, sums)
        return max_sum


if __name__ == '__main__':
    nums = [1, 2, -3, 2]
    print(maxSubArray(nums))
