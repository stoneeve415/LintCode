"""
@title: 82 83 84 824, 落单的数
@author: evestone
"""


def singleNumber1_1(A):
    mhash = {}
    for i in A:
        if i in mhash:
            mhash[i] = True
        else:
            mhash[i] = False
    for key, value in mhash.items():
        if not value:
            return key

    return -1


# 异或性质
def singleNumber1_2(A):
    ans = 0
    for i in A:
        ans = ans ^ i
    return ans


def singleNumber2(A):
    mhash = {}
    for i in A:
        if i in mhash:
            mhash[i] += 1
        else:
            mhash[i] = 1
    for key, value in mhash.items():
        if value == 1:
            return key

    return -1




def singleNumber3(A):
    mhash = {}
    res = []
    for i in A:
        if i in mhash:
            mhash[i] += 1
        else:
            mhash[i] = 1
    for key, value in mhash.items():
        if value == 1:
            res.append(key)

    return res


if __name__ == "__main__":
    A = [1, 1, 2, 2, 3, 4, 4]
    print(singleNumber2(A))
    A = [1, 2, 3, 3, 2, 4, 1, 5]
    print(singleNumber3(A))
