names={'Mike':95, 'Bob':77, 'Ken':89}
print(names)

print(names['Bob'])
#用key赋值
names['Adam']=67
print(names)
#刷新
names['Adam']=68
print(names)

#key不存在的情况
if 'Thomas'in names:
    print(names['Thomas'])

print(names.get('Thomas'))
print(names.get('Thomas', -1))

#删除key
print(names)
print(names.pop('Bob'))
print(names)