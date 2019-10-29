#demo0711.py
import pickle
BasePath='c:\\data\\'
with open(BasePath+'object.dat','wb') as filedump:
    obj1 = 'Test'
    obj2 = ('Justfortest',dict(name='张三', score=dict(语文=100,数学=123,英语=88)))
    pickle.dump(obj1, filedump)
    pickle.dump(obj2, filedump)
