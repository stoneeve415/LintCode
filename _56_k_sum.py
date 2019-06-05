"""
@title: 56 57 58,K个数之和
@author: evestone
"""

'''
2-sum
'''

# 使用hash表
# 2-sum
def two_sum(arr, target):
    hash = {}
    for i, item in enumerate(arr):
        if target-item in hash:
            return [hash[target-item], i]
        hash[item] = i
    return [-1, -1]


# 遍历即可
# 2-sum
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def two_sum_bst(root, target):
    stack = []
    sets = set()
    while root is not None or len(stack) != 0:
        while root is not None:
            val = root.val
            if val in sets:
                return [val, target-val]
            sets.add(target - val)
            stack.append(root)
            root = root.left
        root = stack.pop(-1).right

# 头尾指针
# 2-sum sorted array
def two_sum_arr(nums, target):
    _len = len(nums)
    left = 0
    right = _len - 1
    while left < right:
        _sum = nums[left] + nums[right]
        if _sum > target:
            right -= 1
        elif _sum < target:
            left += 1
        else:
            return [left+1, right+1]
    return []


'''
3-sum
'''


# 一层循环加两个头尾指针
# 3-sum
def three_sum(numbers):
    numbers.sort()
    res = []
    for k, item in enumerate(numbers[:-2]):
        # 最小数大于0 结束
        if numbers[k] > 0:
            break
        # 去掉重复
        if k > 0 and numbers[k] == numbers[k - 1]:
            continue
        target = -item
        i, j = k+1, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                res.append([numbers[k], numbers[i], numbers[j]])
                i += 1
                j -= 1
                # 去掉重复
                while i < j and numbers[i] == numbers[i-1] and numbers[j] == numbers[j+1]:
                    i += 1
                    j -= 1
    return res


# 一层循环叫两个头尾指针
# 3-sum-c
def three_sum_c(numbers, target):
    numbers.sort()
    min_gap = 65536
    for k, item in enumerate(numbers[:-2]):
        # 去掉重复
        if k > 0 and numbers[k] == numbers[k - 1]:
            continue
        i, j = k+1, len(numbers)-1
        while i < j:
            gap = numbers[k] + numbers[i] + numbers[j] - target
            if abs(min_gap) > abs(gap):
                min_gap = gap
            if gap > 0:
                j -= 1
            elif gap < 0:
                i += 1
            else:
                min_gap = 0
                return min_gap + target
    return min_gap + target


# 一层循环加两个头尾指针
# 3-sum-triangle
def triangle_count(S):
    S.sort()
    count = 0
    # ite为当前最大值
    for k, item in enumerate(S[2:],start=2):
        i, j = 0, k-1
        while i < j:
            if S[i]+S[j] > item:
                count += j-i
                j -= 1
            else:
                i += 1
    return count


'''
4-sum
'''


# 两层循环加两个头尾指针
# 4-sum
def four_sum(numbers, target):
    numbers.sort()
    res = []
    for k, item1 in enumerate(numbers[:-3]):
        # 去掉重复
        if k > 0 and numbers[k] == numbers[k - 1]:
            continue
        for m, item2 in enumerate(numbers[k+1:-2],start=k+1):
            # 去掉重复
            if m > k+1 and numbers[m] == numbers[m - 1]:
                continue
            tar = target - item1 - item2
            i, j = m+1, len(numbers)-1
            while i < j:
                if numbers[i] + numbers[j] > tar:
                    j -= 1
                elif numbers[i] + numbers[j] < tar:
                    i += 1
                else:
                    res.append([numbers[k], numbers[m], numbers[i], numbers[j]])
                    i += 1
                    j -= 1
                    # 去掉重复
                    while i < j and numbers[i] == numbers[i-1] and numbers[j] == numbers[j+1]:
                        i += 1
                        j -= 1
    return res


if __name__ == '__main__':

    two_1 = 2
    # # 两数之和
    # arr = [2, 7, 11, 15]
    # target = 9
    # print(two_sum(arr, target))

    two_2 = 2
    # # 两数之和BST树
    # root = TreeNode(4)
    # for i in range(1,9):
    #     name = 'node' + str(i)
    #     locals()[name] = TreeNode(i)
    # root.left = node2
    # root.right = node6
    # node2.left = node1
    # node2.right = node3
    # node6.left = node5
    # node6.right = node7
    # node7.right = node8
    # target = 9
    # print(two_sum_bst(root, target))

    two_3 = 2
    # nums = [2, 7, 11, 15]
    # target = 9
    # print(two_sum_arr(nums, target))

    three_1 = 3
    # # 三数之和
    # arr = [-8,0,-7,-101,-123,-1,-2,0,-1,0,-1111,0,-1,-2,-3,-4,-5,-6,-100,-98,-111,-11]
    # print(three_sum(arr))

    three_2 = 3
    # # 最近三数之和
    # arr = [2, 7, 11, 15]
    # target = 3
    # print(three_sum_c(arr, target))

    three_3 = 3
    S = [3, 4, 6, 7]
    print(triangle_count(S))

    four_1 = 4
    # # 四数之和
    # arr = [1, 0, -1, 0, -2, 2]
    # target = 0
    # print(four_sum(arr, target))
