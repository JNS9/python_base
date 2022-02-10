# dict 순서 x 중복 x 수정 o  삭제 o
# 시퀀스 아니라 순서 없음 슬라이싱 인덱스 안됨

tmpDict = {
    'name' : 'nsjung' ,
    'phone': '01026238169' ,
    'birth': '930409'
}

print('type - ' , type(tmpDict), tmpDict)

print('name' in tmpDict)

tmpDict = {
    '메로나' : [300, 20],
    '비비빅' : [400, 20]
}

print('{}'.format(tmpDict['메로나'][0]))
print('{}'.format(tmpDict['메로나'][1]))
tmpDict['메로나'] = [500, 50]
print('data - ' , tmpDict)

melonaLst = tmpDict['메로나']
melonaLst[0] = melonaLst[0] * 1.1
print(tmpDict)

tmpDict = {
    'Name' : '정남숴이',
    'City' : '서울',
    'Age'  : 50,
    'Grade': 'A+',
    'Status': True
}

tmpDict['Name'] = '정남선'
print(tmpDict)

print(tmpDict['Name'])


tmpDict = dict([
    ('city', '서울'), ('age', 50)
])

print(type(tmpDict), tmpDict)
print(tmpDict['city'])
print(tmpDict.get('Age', '없업서어~'))

tmpDict = dict(
    city = 'seoul' ,
    age = 50
)

print(type(tmpDict), tmpDict)

print(tmpDict['city'])
print(tmpDict.get('Age' , '없어용'))


tmpDict['name'] = '정남서니이잉'
tmpDict.update({'name' : '정남선허허허허허'})
print('data - ' , tmpDict)

keyss = ('apple', 'pear', 'peach')
valuess = (1000, 1500, 2000)

zipDict = dict(zip(keyss,valuess))

for key in zipDict.keys() : # 키를 가져옴  키 : 값
    print(key, zipDict.get(key)) # 값을 가져오고

for value in zipDict.values() :
    print(value)

for key , value in zipDict.items() :
    print(' {} : {} '.format(key, value))

print(zipDict.pop('pear'))

zipDict.clear()
print(zipDict)


