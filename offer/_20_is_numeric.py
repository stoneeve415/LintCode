# -*- coding: utf-8 -*-
"""
@title: 判断字符串是否为数值
@author: evestone
"""


# A[.B]][e|EC] 或者 .B[e|EC]
# 其中A，C表示带正负号的0~9 B表示不带正负号的0~9
def isNumeric(s):
    if len(s) == 0:
        return False
    hasE = False
    hashD = False
    for i in range(len(s)):
        if s[i] in '+-':
            if i == 0:# 首尾是正负号
                continue
            elif s[i-1] in 'eE' and i < len(s)-1 and '0' <= s[i+1] <= '9': # eE后面接正负号
                continue
            else:
                return False
        elif s[i] in '.': # 小数点只能出现一次
            if not hashD:
                hashD = True
            else:
                return False
        elif s[i] in 'eE':
            if not hasE:
                hasE = True
                # 前面必须接数字或小数点 后面必须接正负号或数字0~9
                if i < len(s)-1 and ('0' <= s[i+1] <= '9' or s[i+1] in '+-') and (i != 0 and (s[i-1] == '.' or '0' <= s[i-1] <= '9')):
                    continue
                else:
                    return False
            else:
                return False

        elif s[i] < '0' or s[i] > '9':
            return False
    return True


if __name__ == '__main__':
    str = "1.e-1"
    print(isNumeric(str))