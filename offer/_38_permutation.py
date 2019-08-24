"""
@title: 15,16, 全排列
@author: evestone
"""

# 全排列不包含重复数字 递归实现
def perm_1_1(nums):
    res = []

    def recursive(nums, start, end):
        if start == end - 1:
            res.append(nums.copy())
        else:
            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]
                recursive(nums, start + 1, end)
                nums[i], nums[start] = nums[start], nums[i]

    recursive(nums, 0, len(nums))
    return res


# 全排列包含重复数字 递归实现
def perm_1_2(nums):
    res = []

    def recursive(nums, start, end):
        if start >= end - 1:
            res.append(nums.copy())
        else:
            for i in range(start, end):
                if i == start or not nums[i] in nums[start:i]:  # remove duplicate
                    nums[i], nums[start] = nums[start], nums[i]
                    recursive(nums, start + 1, end)
                    nums[i], nums[start] = nums[start], nums[i]

    recursive(nums, 0, len(nums))
    return res


# 全排列不包含重复数字 非递归实现
def perm_2_1(nums):
    if not nums:
        return [[]]
    result = []
    queue = [[i] for i in nums]
    while queue:
        last = queue.pop(0)
        if len(last) == len(nums):
            result.append(last)
            continue
        for n in nums:
            if n not in last:
                queue.append(last + [n])
    return result


# 全排列包含重复数字 非递归字典序算法实现
def perm_2_2(nums):
    nums.sort()
    res = []
    len_ = len(nums)
    res.append((nums.copy()))
    while True:
        low = len_ - 1
        while low > 0 and nums[low - 1] >= nums[low]:
            low -= 1
        if low <= 0:
            break
        low -= 1
        high = low + 1
        while high < len_ and nums[high] > nums[low]:
            high += 1
        high -= 1
        nums[low], nums[high] = nums[high], nums[low]
        nums[low + 1:] = reversed(nums[low + 1:])
        res.append(nums.copy())
    return res


#  自定义排序规则
def cmp(a, b):
    if a > b:
        return -1
    if a < b:
        return 1
    return 0


if __name__ == '__main__':
    arr = [1, 1, 2]
    # print(perm_1_1(arr))
    print(perm_1_2(arr))
    #
    # print(perm_2_1(arr))
    print(perm_2_2(arr))

    # print(sorted(arr, key=functools.cmp_to_key(cmp)))
