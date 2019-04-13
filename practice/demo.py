import os
import keyword

'''
内置关键字
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

r = keyword.kwlist
print(r)



str='Runoob'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


import sys,time
for i in sys.argv:
	print(i)
print('\n python 路径为',sys.path)

from sys import *

print(argv)
print(path)


a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))

'''
String
List
Tuple
Set
Dictionary
'''

print({'Tom','Jim','Tom'})


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket

a,b = 0,1
while b < 10:
	print(b,end=',')
	a,b=b,a+b

