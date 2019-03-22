#!/usr/bin/python3

# 计算1到99中除88以外的和
one = 1
sum = 0
while one < 100 :
    if one != 88 :
        sum += one
        print(one)
    one += 1
print(sum)
