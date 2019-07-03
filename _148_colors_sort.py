# -*- coding: utf-8 -*-
"""
@title: 148.143 颜色排序
@author: evestone
"""

'''
三种颜色
'''


# 三指针法
def sortColors1(nums):
    n = len(nums)
    if n <= 1:
        return nums
    left, right = 0, n-1
    cur = 0
    while cur <= right:
        if nums[cur] == 0:
            nums[cur], nums[left] = nums[left], nums[cur]
            left += 1
            if left > cur:
                cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[right] = nums[right], nums[cur]
            right -= 1
        else:
            cur += 1
    return nums


'''
k种颜色
'''


# 彩虹排序
def sortColors2(nums, k):
    n = len(nums)
    if n <= 1:
        return nums

    def rainbow(nums, start, end, colorFrom, colorTo):
        if start >= end or colorFrom >= colorTo:
            return

        left, right = start, end
        mid = (colorFrom + colorTo) // 2
        while left <= right:
            while left <= right and nums[left] <= mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        rainbow(nums, start, left, colorFrom, mid)
        rainbow(nums, right, end, mid+1, colorTo)

    rainbow(nums, 0, n-1, 1, k)
    return nums


if __name__ == '__main__':
    nums1 = [1, 0, 1, 2]
    print(sortColors1(nums1))

    nums2 = [3, 2, 2, 1, 4]
    k = 4
    print(sortColors2(nums2, k))