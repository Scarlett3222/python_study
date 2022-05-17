# coding=UTF-8
#开始梳理python语法
import os
import requests
from bs4 import  BeautifulSoup as bs



def main():
    # 感受Python变量类型
    temp = 18.6
    print("temp的类型是：" + str(type(temp)) + "，temp的值是：" + str(temp))
    orig = temp
    print("orig的类型是：" + str(type(orig)) + "，orig的值是：" + str(orig))
    temp = temp + 1
    print("temp修改后的值是：" + str(temp))
    print("修改temp后，orig的值是：" + str(orig))

def typeOfPython():
    # Python内置的类
    typePython = input("请输入一种Python内置类的数据类型（bool、int、float、list、tuple、str、set、dict）：")
    if typePython == "bool":
        print("bool类只有两个值：True和False，构造函数bool()默认返回False；0和空也表示False，其他表示True")
    elif typePython == "int" or typePython == "float":
        print("int和float是最主要的两个数值类型，构造函数int()返回0；float()返回0.0")
        print("int('非数字')会抛出ValueError，例如：")
        try:
            int("hello")
        except ValueError:   
            print("抛出了ValueError")
        except ZeroDivisionError:
            print('0不能做除数')
        except:
            print("没有预料到的错误")
        finally:  # 无论是否有异常，都会执行的代码
            print("程序结束")
    elif typePython == "list":
        print("list实例存储对象序列，列表是一个参考结构，在技术上存储元素的引用序列。列表采用0索引，因此一个长度为n的列表包含从0到n-1的元素。构造函数list()产生一个空列表，python使用[]作为列表的分隔符")
    elif typePython == "tuple":
        print("tuple是序列的一个不可变版本，Python使用()作为元组的分隔符。为了与带括号的表达式区别开，只有一个元素的元组表示为(17,)，元素后必须有一个逗号")
    elif typePython == "str":
        print("str专门用来代表一种不变的字符序列，它基于Unicode国际字符集。字符串里可以使用反斜杠作为转义字符，比如'20 \\u20AC'可以表示20 \u20AC")
    elif typePython == "set":
        print("set表示一个集合的数学概念，即许多元素的集合，集合中没有重复元素，而且这些元素没有内在联系。--只有不可变类型的实例才可以被添加到集合里。构造函数set()表示一个空集合，集合用{}作为集合的分隔符")
    elif typePython == "dict":
        print("dict表示字典或者映射，即从一组不同的键中找到对应的值，构造函数可用{}")
    else:
        print("没有该数据类型")

def pinglun():
    url = "https://appgallery.huawei.com/app/C10374976?sharePrepath=ag&locale=zh_CN&source=appshare&subsource=C10374976&shareTo=weixin&shareFrom=appmarket"
    res = requests.get(url)
    print(res.text)



if __name__ == '__main__':
    # main()    # 感受Python变量类型
    # typeOfPython()    # Python内置的类
    pinglun()