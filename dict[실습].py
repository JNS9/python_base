# 단어의 빈수를 구하기
# 출력 결과 : {'love' : 2, 'word' : 2 , 'cat' : 1}

word_vec = ['love','word','love','cat','word']
print('len - ', len(word_vec))
# case 01, dictionary 함수 이용
wc = {}
for word in word_vec :
    wc[word] = word_vec
print(wc)
# case 02, list 함수 이용
# case 03, for if문 사용
#case 04
# case 05

# set, zip

print('comprehension - ', [word_vec.count(int) for i in set(word_vec)])
result = dict(zip(set(word_vec), [word_vec.count(i) for i in set(word_vec)]))
print('case 05 wc -' , result)

