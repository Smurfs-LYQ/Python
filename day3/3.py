#!/usr/bin/python3

# for循环

a = 'abcdefghijklmnopqrstuvwxyz'
for i in a :    # i代表的是迭代中赋值的变量，a代表的是可迭代对象
    print(i)

# 检测字符串中是否 有/没有 指定的元素  in/not in
a = 'one two thr'
if 'two' in a :    # 'two'代表的是指定的元素，a代表的是要检测的对象
    print('YES')
