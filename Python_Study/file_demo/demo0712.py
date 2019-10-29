BasePath='c:\\data\\'
import pickle
with open(BasePath+'object.dat','rb') as fileload:
    obj1 = pickle.load(fileload)
    obj2 = pickle.load(fileload)
    print(type(obj1),str(obj1))
    print(type(obj2),str(obj2))
