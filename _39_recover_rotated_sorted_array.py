"""
@title: 39. 恢复旋转有序矩阵
@author: evestone
"""

'''
方法一
'''


def search_min1(nums):
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] == nums[right]:
            right = right - 1
        else:
            left = mid
    if nums[left] < nums[right]:
        return left
    else:
        return right


def recoverRotatedSortedArray1(nums):
    # write your code here
    length = len(nums)
    if length <= 1:
        return nums
    min_i = search_min1(nums)
    #     print(min_i)
    if min_i < len(nums) // 2:
        for i in range(min_i):
            temp = nums[0]
            del nums[0]
            nums.append(temp)
    else:
        for i in range(length - min_i):
            temp = nums[length - 1]
            del nums[length - 1]
            nums.insert(0, temp)
    return nums


'''
方法二
'''


# 三步旋转法
def search_min2(nums):
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] == nums[right]:
            right = right - 1
        else:
            left = mid
    if nums[left] < nums[right]:
        return left
    else:
        return right


def reverse(nums, start, end):
    i, j = start, end
    while i < j:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        i += 1
        j -= 1


def recoverRotatedSortedArray2(nums):
    # write your code here
    length = len(nums)
    if length <= 1:
        return nums
    min_i = search_min2(nums)
    reverse(nums, 0, min_i - 1)
    reverse(nums, min_i, length - 1)
    reverse(nums, 0, length - 1)
    return nums


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(len(nums))
    print(recoverRotatedSortedArray2(nums))
    