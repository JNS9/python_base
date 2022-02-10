import random

word = 'Beautiful'
for w in word :
    print(w, end='\t')
print()

for idx, w in enumerate(word) :
    print(idx, w, end='\t')
print()

myInfo = {
    'name': 'seop' ,
    'Age': '50',
    'City': 'Seoul'
}

for key in myInfo :
    print(key, myInfo[key] , end='\n')
print()

for key , value in myInfo.items() :
    print(key, value , end='\t')
print()

numbers = [14, 3, 4, 7, 6, 23, 24, 59, 23, 19, 8]
# break , continue

if 24 in numbers :
    print('Ture')
else :
    print('False')

for idx, num in enumerate(numbers) :
    if num == 24 :
        print(idx, 'Found')
    else :
        print(idx, 'Not Found')

for num in numbers :
    if num == 25 :
        print('Found!!')
        break
else :
    print('Not Found!!')

for row in range(2,10) :
    if row == 5 :
        continue
    for col in range(1, 10) :
        print('{} * {} = {}'.format(row,col,row*col) , end=('\t'))
    print()




str = \
'''
저는 파이썬을 강의 중인 강사 임정섭입니다.
주소는 서울시 입니다.
나이는 숫자에 불과합니다.
'''

sentences = []
words = []
for s in str.split('\n') :
    sentences.append(s)
    for w in s.split() :
        words.append(w)
print(sentences, len(sentences))
print(words , len(words))

apt = [
    ['101호' , '102호'] ,
    ['201호' , '202호'] ,
    ['301호' , '302호']
]

for row in apt :
    for col in row :
        print(col)
    print('*' * 50)

