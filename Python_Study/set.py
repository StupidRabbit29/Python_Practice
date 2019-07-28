#用list作为set的输入集合
s1=set([1, 2, 3])
print(s1)
#过滤重复元素
s2=set([1, 1, 2, 2, 3, 3, 4])
print(s2)

#add不会重复添加
s1.add(5)
print(s1)
s1.add(5)
print(s1)

#删除元素
s2.remove(4)
print(s2)

#两个集合可以求交集，并集
print(s1&s2)
print(s1|s2)


#测试list和tuple
s3=set(['a', 2])
print(s3)
s3.add(('a', 'b', ('A', 'B')))
print(s3)
print('zhuqianye is pig')