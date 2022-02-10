# ----[실습]
movie_lst = ['이터널스', '스파이더맨', '매트릭스', '경관의 피', '샹치', '스타워즈', '아이언맨']
print('type -', type(movie_lst))
print('data -', movie_lst)

'''
요구사항
1. 모가디슈를 추가
2. 스파이더맨과 매트릭스 사이에 임섭순을 추가
3. 경관의 피를 삭제
4. 매트릭스와 샹치를 삭제
5. 이터널스의 인덱스를 구해서 pop() 함수를 이용한 삭제
6. 최종리스트 출력
'''

movie_lst.append('모가디슈') #1
movie_lst.insert(2,'임섭순') #2
movie_lst.remove('경관의 피') #3

del movie_lst[3] #4
del movie_lst[3]
print(movie_lst)

idx = movie_lst.index('이터널스') #5
movie_lst.pop(idx)
print(movie_lst)



