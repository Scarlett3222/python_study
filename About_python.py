#开始梳理python语法
import os


def main():
    temp = 18.6
    print("temp的类型是：" + str(type(temp)) + "，temp的值是：" + str(temp))
    orig = temp
    print("orig的类型是：" + str(type(orig)) + "，orig的值是：" + str(orig))
    temp = temp + 1
    print("temp修改后的值是：" + str(temp))
    print("修改temp后，orig的值是：" + str(orig))

def typeOfPython():
    typePython = input("请输入数据类型：")
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
    else:
        print("没有该数据类型")


if __name__ == '__main__':
    typeOfPython()