#ord()获取字符整数表示
#chr(将编码转换为对应的字符
print(ord('中'))
print(ord('A'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')
print('hello, %s'%'world')
print('Hi, %s, you have $%d'%('Fu Bin', 10000))
#补0或补空格
print('%2d-%02d'%(3, 1))
print('%2d-%2d'%(3, 1))
#小数位数
print('%.2f'%3.1415926)
#%s可以将任何数据类型转换为字符串
print('Age:%s, Gender:%s'%(25, True))
#打印%
print('%d%%'%7)
#format()格式化输出
print('Hello, {0}, {1:.1f}%'.format('Fu', 3.1415926))


before=72
now=85
ratio=(now-before)/before
print('%2.1f'%ratio)