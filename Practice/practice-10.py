import math

def estimated(choice,size,other):
    if choice == 1:
        number = math.ceil(size * 80 / other)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,other,number))  
    elif choice == 2:
        time = size * 80 / other
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,other,time))  

def my_input():
     choice = int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
     size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
     if choice==2:
         other = int(input('请输入人力数量：（请输入整数）'))
     elif choice == 1:
         other = float(input('请输入工时数量：（请输入小数）'))
     estimated(choice,size,other)
my_input()
