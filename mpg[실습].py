import mpg
import mpg as m
from statistics import mean

mpgLst = []
with open('./data/mpg.txt' , 'r' , encoding='utf-8') as file :
    file.readline()
    line = file.readline()
    while line != '' :
        row = line.strip('\n').split(',')
        mpgLst.append(row)
        line = file.readline()
#    for f in file :
#        print(f)

mpg.Mpg.