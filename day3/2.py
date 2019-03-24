#!/usr/bin/python3

# 字符串操作

# 首字母大写
a = 'one'
print(a.capitalize())

# 所有字母大写
a = 'OnE'
print(a.upper())

# 所有字母小写
a = 'oNe'
print(a.lower())

# 大小写翻转
a = 'OnE'
print(a.swapcase())

# 每个单词的首字母大写
a = 'one two thr'
print(a.title())

# 将字符串按照指定字符填充为指定长度(从两侧填充)
a = 'one'
print(a.center(5,'-'))    # 5代表的是规定字符串的长度，'-'代表的是用-填充(不写默认为None，也就是空格)

# 检测长度(公共方法)
a = 'one'
print(len(a))

# 判断字符串指定区域是否以指定字符开头(startswith)/结尾(endswith)
a = 'one two thr'
print(a.startswith('o',0,3))    # 'o'代表的是是否以o开头，0代表的时从第0位开始(不写默认从头开始)，3代表的是到截取几位(不写默认一直到末尾)，第2、3位参数类似于切片

# 检测指定元素在指定字符串中的第一次出现的位置，找不到返回-1，index函数的功能跟find一样区别在于index找不到会报错
a = 'one two thr'
print(a.find('t',0,5))    # 't'代表的是要查找的元素，0代表的时从第0位开始(不写默认从头开始)，5代表的是到截取几位(不写默认一直到末尾)，第2、3位参数类似于切片

# 去除字符串左右两侧的指定字符 lstrip:去除字符串左侧的指定字符 rstrip:去除字符串右侧的指定字符
a = '*o*n#'
print(a.strip('#*'))    # '#*'代表的是去除字符串两侧的#和*，不写默认去除的时空格

# 检测字符串中指定区域出现过指定元素的次数
a = 'one two thr'
print(a.count('o',0,7))    # 'o'代表的是要检测的元素，0代表的时从第0位开始(不写默认从头开始)，7代表的是到截取几位(不写默认一直到末尾)，第2、3位参数类似于切片

# 将字符串按照指定的规则分割成列表
a = 'one-two-thr'
print(a.split('-'))    # '-'代表的是以-为标志进行分割

# 字符串替换
a = 'one *wo *hr'
print(a.replace('*','t',1))    # '*'代表的是要替换的字符，'t'代表的是替换后的字符，1代表的是替换几个

# format的三种玩法，格式化输出
a = '我是{},今年是{}年'.format('Smurfs的格格巫',2019)
print(a)
a = '我是{1},今年是{0}年'.format(2019,'Smurfs的格格巫')    # {1}代表的是取format中的第一位信息，{0}代表的是取format中的第零位信息
print(a)
a = '我是{name},今年是{year}年'.format(name='Smurfs的格格巫',year=2019)    # {name}代表的是取format中下标是name的信息，{year}代表的是取format中下标是year的信息
print(a)

# is系列
a = 'one'
print(a.isalpha())    #字符串是否只由字符串组成
a = '123'
print(a.isdigit())    #字符串是否只由数字组成
a = 'one123'
print(a.isalnum())    #字符串是否由字母和数字组成
