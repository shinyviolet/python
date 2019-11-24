import random
for i in range(1,11):
    answer = random.sample('ABCD',1)
    print('第%d题的答案为%s' %(i,answer))
    print(type(answer))