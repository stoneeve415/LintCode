"""
@title: 5.第k大的元素
@author: evestone
"""


import heapq as hq


# 快排思想
def search_k(k, nums, left, right):
    i = left
    j = right
    length = right - left + 1
    temp = nums[i]
    while i < j:
        while nums[j] >= temp and i < j:
            j -= 1
        nums[i] = nums[j]
        while nums[i] < temp and i < j:
            i += 1
        nums[j] = nums[i]
    nums[i] = temp
    if i == k-1:
        return temp
    elif i > k-1:
        return search_k(k, nums, left, i-1)
    else:
        return search_k(k, nums, i+1, right)


def kthLargestElement(n, nums):
    # write your code here
    length = len(nums)
    if length < n:
        return -1
    return search_k(len(nums)-n+1, nums, 0, length - 1)

# k小元素
def kthSmallest(k, nums):
    # write your code here
    if len(nums) < 1 or len(nums) < k:
        return -1
    k -= 1

    def recur(nums, left, right):
        l, r = left, right
        if l > r:
            return -1
        while l < r:
            while l < r and nums[r] > nums[l]:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
            while l < r and nums[l] <= nums[r]:
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        if l == k:
            return nums[l]
        elif l < k:
            return recur(nums, l + 1, right)
        else:
            return recur(nums, left, l - 1)

    return recur(nums, 0, len(nums) - 1)

# 最小堆实现
def kthLargestElement2(n, nums):
    heap = []
    for i,item in enumerate(nums):
        if i < n:
            hq.heappush(heap, item)
        else:
            if item > heap[0]:
                hq.heapreplace(heap, item)
    return heap[0]


if __name__ == '__main__':
    n = 3
    nums = [9, 3, 2, 4, 8, 6, 6]
    print(kthLargestElement(n, nums))

    # heapq用法
    heap = []
    hq.heappush(heap, 3)
    hq.heappush(heap, 1)
    hq.heappush(heap, 9)
    print(len(heap))
    print(heap[0])
    hq.heapreplace(heap, 2)
    print(heap[0])

    A = [2, 5, 1, 9, 6]
    hq.heapify(A)
    print(A[0])
    print(hp.nlargest(2, A))
    print(hp.nsmallest(2, A))