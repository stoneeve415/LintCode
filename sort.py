

def bubble(nums):
    _len = len(nums)
    for i in range(_len-1):
        j = 1
        while j < _len-i:
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            j += 1
    return nums


def select(nums):
    _len = len(nums)
    for i in range(_len - 1):
        k = -65536
        for j in range(_len-i):
            if nums[j] > k:
                k = nums[j]
                index = j
        nums[index], nums[_len-i-1] = nums[_len-i-1], nums[index]
    return nums


def insert(nums):
    _len = len(nums)
    for i in range(1, _len):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums


def quick(nums):
    _len = len(nums)

    def recursive(nums, start, end):
        if start >= end:
            return
        left, right = start, end
        while left < right:
            while left < right and nums[right] >= nums[left]:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            while left < right and nums[left] <= nums[right]:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        recursive(nums, start, left)
        recursive(nums, left+1, end)
    recursive(nums, 0, _len-1)

    return nums


def merge(nums):
    _len = len(nums)

    def merge(nums, left1, right1, left2, right2):
        temp =[]
        start, end = left1, right2
        while left1 <= right1 and left2 <= right2:
            if nums[left1] < nums[left2]:
                temp.append(nums[left1])
                left1 += 1
            else:
                temp.append(nums[left2])
                left2 += 1
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


def shell(nums):
    _len = len( nums)
    gap = _len // 2
    while gap > 0:
        i = gap
        while i < _len:
            j = i
            while j >= gap and nums[j-gap] > nums[j]:
                nums[j-gap], nums[j] = nums[j], nums[j-gap]
                j -= gap
            i += gap
        gap = gap // 2
    return nums

# def ttt(s1, s2, s3):
#     # write your code here
#     i, j, k = 0, 0, 0
#     l1, l2, l3 = len(s1), len(s2), len(s3)
#     if l1 + l2 != l3:
#         return False
#     while True:
#         if i < l1 and s1[i] == s3[k]:
#             i += 1
#             k += 1
#         elif j < l2 and s2[j] == s3[k]:
#             j += 1
#             k += 1
#         else:
#             break
#     if i == l1 and j == l2 and k == l3:
#         return True
#     return False






if __name__ == '__main__':
    nums = [5, 2, 5, 1, 9, 7, 22, 4]
    print(bubble(nums.copy()))
    print(select(nums.copy()))
    print(insert(nums.copy()))
    print(quick(nums.copy()))
    print(merge(nums.copy()))
    print(shell(nums.copy()))


