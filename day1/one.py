#!/usr/bin/python3

'''
# 打印1,2,3,4,5,6,8,9,10
one = 1
while one <= 10 :
    if one == 7 :
        one += 1
        continue
    print(one)
    one += 1
'''

'''
# 求1-100所有数的和
one = 1
two = 0
while one <= 100 :
    two += one
    one += 1
print(two)
'''

# 打印100以内所有的奇数
'''

# 方法1
one = 1
while one <= 100 :
    if one % 2 :
        print(one)
    one += 1

# 方法2
one = 1
while one <= 100 :
    print(one)
    one += 2
'''

# 打印100以内所有的偶数
'''
one = 1
while one <= 100 :
    if one % 2 == 0 :
        print(one)
    one += 1
'''

# 求1-2+3-4...99的所有数的和
'''
one = 1
two = 0
while one < 100 :
    if one % 2 == 0:
        two -= one
    else :
        two += one
    one += 1
print(two)
'''

# 用户登录(三次登录机会)
'''
# 面向过程
one = 1
while one <= 3 :
    username = input('请输入username: ')
    password = input('请输入password: ')
    if username == 'test' and password == '123' :
        print('登录成功')
        break
    else :
        print('登录失败请重试')
        one += 1
'''

'''
# 面向对象
class user_pwd :
    def __init__(self) :
        self.username = input('请输入username: ')
        self.password = input('请输入password: ')
one = 1
while one <= 3:
    add = user_pwd()
    if add.username == 'test' and add.password == '123' :
        print('登录成功')
        break
    else :
        print('输入错误请重试')
        one += 1
'''
