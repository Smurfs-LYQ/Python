#!/usr/bin/python3

# 用户交互
one = int(input('请输入一个数字：'))

# if判断
if one == 1 :
    print('1')
elif one == 2 :
    print('2')
else :
    print('3...')

# while循环
while one <= 10 :
    print(one)
    one += 1

# while...else
'''
# else会在循环结束的时候执行，前提是不能被break打断
one = 1
while one <= 10 :
    print(one)
    one += 1
else :
    print('循环结束')
'''
