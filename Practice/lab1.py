file1 = open('abc/winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()
print(file_lines)
dict_scores = {}
list_scores = []
final_scores = []
test_scores=[]
for line in file_lines:
    name=line[:-4]
    score=line[-4:-1]
    print(name+':'+score)
    dict_scores[score]=name
    list_scores.append(score)
print(list_scores)
list_scores.sort(reverse=True)
print(list_scores)
for score in list_scores:
    result=dict_scores[score]+str(score)+'\n'
    final_scores.append(result)
print(final_scores)
with open('winner_new.txt','w') as file2:
    file2.writelines(final_scores)