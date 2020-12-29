from java import jclass
import tushare


def greet(name):
    print("--- hello,%s ---" % name)
    data = tushare.get_realtime_quotes('600000')
    print(data)

def add(a,b):
    return a + b

def sub(count,a=0,b=0,c=0):
    return count - a - b -c

def get_list(a,b,c,d):
    return [a,b,c,d]

def print_list(data):
    print(type(data))
    print(data.size())
    # 遍历Java的ArrayList对象
    for i in range(data.size()):
        print(data.get(i))

# python调用Java类
def get_java_bean():
    JavaBean = jclass("com.wwb.test.python.JavaBean")
    jb = JavaBean("python")
    jb.setData("json")
    jb.setData("xml")
    jb.setData("xhtml")
    return jb