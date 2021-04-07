from collections import defaultdict
'''defaultdict为字典中不存在的键赋予默认的值
   defaultdict()内部可以接受类型，也可以接受
   无参数的函数，并且以该函数的返回值为参数
   若函数无返回值(即函数的返回值为none),即默认值
   为None

def hello():
    print("hello")

dd = defaultdict(hello)

print(dd["enhen"])
'''

#命名元组，为含有属性的元组
from collections import namedtuple
# "enhen"为该命名元组的名称
# nametuple返回一个类似类的东西，同元组一样，其内容不可更改
stock = namedtuple("enhen", ["weight","height"])
s = stock(100,200)
print(s)

#示例字典
Bucket = {"GOOG":(23,63,62,72),"MSFT":(25,62,14,26)}

# keys()方法，values()方法返回一个包含字典中所有键和所有值得迭代器
print(Bucket.keys())
print(Bucket.values())

# items()返回一个对字典中每个项目形成的一个如(键，值)对这样的元组的迭代器
for keys,values in Bucket.items():
    print(keys)
    print(values)


# print(Bucket["GOOG"])
# get方法，返回键的值
# 接收一个键作为第一个参数，以及当一个键不存在时的可选默认值
# print(Bucket.get("enhen","eee"))
#get()函数仅仅返回了给的默认值，并没有给不存在的键设置默认值
print(Bucket)
# setdefault()函数当查找的键不存在的时候，将其
#加入字典中，并且设置给定的默认值
Bucket.setdefault("enhen","eeee")
print(Bucket)
