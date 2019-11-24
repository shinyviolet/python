import csv
with open('tes.csv','a',newline='') as csvfile:
    writer=csv.writer(csvfile,dialect='excel')
    header=['小区名称','地址','建筑年份','楼栋','单元','户室','朝向','面积']
    writer.writerow(header)