"""
@title: 1713,邮件过滤
@author evestone
"""

def numUniqueEmails1(emails):
    # write your code here
    print(emails)
    emails_sets = set()
    for email in emails:
        length = len(email)
        temp = ''
        i = 0
        # 标记----0本地名称；1本地名称以‘+’结束；2本地名称以‘@’结束
        flag = 0
        while i < length:
            # 处理本地名称
            if flag == 0:
                if email[i] == '+':
                    flag = 1
                elif email[i] == '@':
                    flag = 2
                elif email[i] != '.':
                    temp += email[i]
             # ‘+’结束，处理域名
            elif flag == 1:
                if email[i+1] == '@':
                    flag = 2
            # ‘@’结束，处理域名
            elif flag == 2:
                temp += email[i:length]
                emails_sets.add(temp)
                break
            i += 1
        return emails_sets


# 更简洁实现
def numUniqueEmails2(emails):
    # write your code here
    emails_sets = set()
    for email in emails:
        local_name, domain_name = email.split('@')
        local_name = ''.join(local_name.split('+')[0].split('.'))
        email = local_name + '@' + domain_name
        emails_sets.add(email)
    return emails_sets


if __name__ == '__main__':
    e = ["test.email+alex@lintcode.com", "test.e.mail+bob.cathy@lintcode.com", "testemail+david@lin.tcode.com"]
    print(numUniqueEmails1(e))
    print(numUniqueEmails2(e))
