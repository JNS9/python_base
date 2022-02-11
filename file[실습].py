
# Que 1
# special_words.txt 파일로부터 줄단위로 문자'c' 포함된 단어를 출력
# 단) 단어를 출력할 때 등장한 순서대로 출력

def que01() :
    with open('./data/special_words.txt' , 'r' , encoding='utf-8') as file :
        lines = file.readline().split()
        #print(type(lines))
        #print(lines)
        lines = [ i.strip(',.') for i in lines]
        #print(lines)
        for word in lines :
            if 'c' in word :
                print(word)
# caller
#que01()




#Que 2
# special_words.txt 파일로부터 단어ㅢ 길이가
# 10 이하인 단어를 출력하고 카운팅하세요

def que02() :
    cnt = 0
    with open('./data/special_words.txt' , 'r' , encoding='utf-8') as file :
        lines = file.readline().split()
        lines = [ i.strip(',.') for i in lines]
        for word in lines :
            if len(word)  <= 5 :
                cnt += 1
                print(word)
        print('5 이하인 단어의 개수 : {} '.format(cnt))

# caller
#que02()


# zipcode.txt
# input() 함수를 이용해서 동 이름을 입력받아
# 예) 개포
# 해당하는 동의 주소를 출력하는 함수를 정의한다
# hint - \t
# startswith() 함수를

# Que 3
# 예외처리
def que03() :
    with open('./data/zipcode.txt', 'r', encoding='utf-8') as file:
        for i in lines :
            lines = file.readline() #.split()
            lines = [ i.strip(',') for lines in lines]
            print(lines)

# caller
#que03()

def que04() :
    word = input()
    with open('./data/zipcode.txt', 'r', encoding='utf-8') as file:
        for word in file :
            for each_line in word :
                if each_line.find(word) >0 :
                    print(each_line)
                else :
                    pass
        # while True :
        #     word = ('개포')
        #     lines = file.readline().startswith(word, 16)
        #     print(lines)
        #     if not lines : break
        # file.close()
#        lines = file.readline().startswith('개포', '\t')
# caller
#que04()


def que05() :
    word = input()
    with open('./data/zipcode.txt', 'r', encoding='utf-8') as file:
        for word in file :
           lines = file.readline().split(',.')
           print([line.rstrip('\t') for line in lines if line.find(word)])

#que05()


def que06() :
    dong = input('동을 입력하세요 예) 개포 : ')
    try :
        with open('./data/zipcode.txt' , 'r' , encoding='utf-8') as file :
            line = file.readline()
            while line :
                addr_lst = line.split('\t')
                if addr_lst[3].startswith(dong) :
                    print(addr_lst)
                line = file.readline()
    except Exception as e :
        print(str(e))

que06()
