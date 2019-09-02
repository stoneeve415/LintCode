# -*- coding: utf-8 -*-
"""
@title: 逆序对数
@author: evestone
"""
res = 0

def merge(nums):
    _len = len(nums)

    def merge(nums, left1, right1, left2, right2):
        global res
        temp =[]
        start, end = left1, right2
        while left1 <= right1 and left2 <= right2:
            if nums[left1] <= nums[left2]:
                temp.append(nums[left1])
                left1 += 1
            else:
                temp.append(nums[left2])
                left2 += 1
                res += right1-left1+1
        if left1 <= right1:
            temp.extend(nums[left1:right1+1])
        if left2 <= right2:
            temp.extend(nums[left2:right2+1])
        nums[start:end+1] = temp

    def m_sort(nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        m_sort(nums, start, mid)
        m_sort(nums, mid+1, end)
        merge(nums, start, mid, mid+1, end)

    m_sort(nums, 0, _len-1)
    return nums


if __name__ == '__main__':
    num = [7, 5, 6, 4]
    merge(num)
    print(res)

