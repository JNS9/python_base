'''
oop(객체 지향 프로그래밍)
- class(변수 + 함수) -> instance로 생성할 수 있다.
-- 클래스에 정의된 변수와 함수는 클래스의 소유가 아닌 인스턴스의 소유이다.
-- initalizer (초기화 함수, 생성자)
-- magic function
- object vs instance
- object - 명사적(변수) 동사적(변수)
- 함수 < 클래스 < 모듈(클래스(변수 + 함수)) < 패키지
- self -> 인스턴스를 대표하는 키워드

'''

tea_name = '임정섭'
tea_subject = 'python'
tea_mail = 'same0525@naver.com'

def printTee() :
    print(tea_name, tea_subject, tea_mail)

class Teacher :
    # 변수 + 함수
    cls_var = 3.5

    def doing(self):
        print('인스턴스 소유의 함수입니다.')

tea = Teacher()

print(tea)
print('instance function -' , end='')
tea.doing()


class Person :
    cls_var = 3.5

    def __init__(self, name, subject, email):
        self.name   = name
        self.subject = subject
        self.email  =   email

    def perInfo(self):
        return '이름 {} , 과목 {} , 메일 {}'.format(self.name, self.subject, self.email)

    def isSocholarShip(self, grade):
        if grade >= Person.cls_var :
            return True
        else :
            return False

per01 = Person('정남선' , '파이썬' , 'same0525@naver.com')
\ㅅㅀㅊㅌㅋ5412ㅂㅁ21`er02 = Person('손정연' , '자바' , '메일입니드앙')
per03 = Person('노희명', 'C++', '메일에ㅣ에용')
#Person.cls_var

lst = list()
lst.append(per01)
lst.append(per02)
lst.append(per03)
for instance in lst :
    print(instance.name)
    print(instance.subject)
    print(instance.email)
    print(instance.isSocholarShip(4.5))
    print(instance.cls_var)