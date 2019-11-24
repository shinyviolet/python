start_floor = input('请输入起始楼层：')
end_floor = input('请输入终止楼层：')
#确定每一单元有几层楼

start_floor_rooms = {}
#创建字典，存放起始楼层所有户室的信息
rooms=int(input('how many rooms in one floor'))

floor_last_number = []
a=1
#创建列表，存放户室的尾号如['01','02','03']，后续楼层可复用
while a <= rooms:
    last_number = str(0)+str(a)
    floor_last_number.append(last_number)
#将元素添加到存放户室尾号的列表里，如floor_last_number = ['01']
    room_number = int(start_floor + last_number)
#户室名为room_number,由楼层start_floor和尾号last_number组成,如'301'
    direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number ))
    if direction == 1:
        direc='南北朝向'
    elif direction == 2:
        direc='东西朝向'
#输入中文比输入数字要麻烦许多，我们可以先用1和2代替

    area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))

    start_floor_rooms[room_number] = [direc,area]
# 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}
    a=a+1
    print(start_floor_rooms)