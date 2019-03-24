#!/usr/bin/python3
# 字符串的索引与切片

a = 'abcdefghijklmnopqrstuvwxyz'

# 索引
print(a[3])    #这里的 3 代表的是字符串中的位置，位置从0开始

print(a[-1])    #这里的 -1 代表的是取字符串中的最后一位

# 切片 顾头不顾尾
print(a[0:4])    #这里的 0和4 代表的是从第0位开始，取4位

print(a[0:])    #这里的 0 代表的是从第0位开始，':'后面不写代表取到末尾
print(a[:])
