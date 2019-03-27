#!/usr/bin/python3

# val = input('请输入要算的数：')

val = '1+2-3*4'
for i in ['+', '-', '*', '/'] :
    res = val.split('%s'%(str(i)))

print(res)
