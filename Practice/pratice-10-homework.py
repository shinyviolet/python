import random

# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)

# 胜负
print('—————结果—————')
def compare(computer_choice, user_choice):
        computer_index=punches.index(computer_choice)
        print(computer_index)
        user_index=punches.index(user_choice)
        print(user_index)
        if computer_index-user_index == 1 or user_index-computer_index == 2:
            return "user"
        elif user_index-computer_index ==1 or computer_index-user_index == 2:
            return "computer"
        else:
            return "no one wins"
winner = compare(computer_choice, user_choice)
print("The winner is %s" % winner)