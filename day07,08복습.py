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
per02 = Person('손정연' , '자바' , '메일입니드앙')
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


print()
print()
class Employee :

    raise_rate = 1.1

    def __init__(self, userName, userSalary):
        print('초기화 함수 작동 중')
        self.userName = userName
        self.userSalary = userSalary

    def getSalary(self):
        return '{}님의 급여는 {} 입니다.'.format(self.userName, self.userSalary)

    def incrementSalary(self):
        self.userSalary = self.userSalary * Employee.raise_rate

# emp0bj01 = Employee('정남선', 1000)
# emp0bj02 = Employee('손정연', 2000)
# print(emp0bj02.getSalary())
# print(emp0bj01.getSalary())
#
# print('급여 인상 -')
# emp0bj01.incrementSalary()
# emp0bj02.incrementSalary()
# print(emp0bj02.getSalary())
# print(emp0bj01.getSalary())
#
# print('급여 인상률 변경 -')
# Employee.raise_rate = 1.5
# emp0bj01.incrementSalary()
# print(emp0bj01.getSalary())

'''
[실습]
- 1. Account class 작성
- 2. 인스턴스 변수         - account(계좌), balance(잔액), interestRate(이자율)
- 3. accountInfo()      - 계좌 정보를 출력하는 함수
- 4. deposit(amount)    - 매개변수 들어온 amount를 balance 입금 
- 5. withDraw(amount)   - 매개변수 들어온 amount를 balance 출금
- 5-1. 단) 잔고가 부족할 경우 ' 잔액이 부족하여 출금이 안돼요'
- 6. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 2자리까지 출력
'''

class Account :

    def __init__(self, account, balance, interestRate):
        self.account        = account
        self.balance        = balance
        self.interestRate   = interestRate

    def accountInfo(self):
        print('계좌번호 : {} 잔액 : {}'.format(self.account , self.balance))

    def withDraw(self, amount):
        if self.balance >= amount :
            self.balance -= amount
        else :
            print('잔고가 부족하여 출금이 불가능합니다.')

    def deposit(self, amount):
        self.balance += amount

    def printInterestRate(self):
        self.balance = self.balance * (1+self.interestRate)
        print('%.2f' % self.balance)

# caller
abc = Account('652702-333-239493' , 500000 , 0.121)
print('계좌정보 출력')

# abc.accountInfo()
# abc.withDraw(300000) # 출금 금액
# abc.accountInfo()
# abc.deposit(200000)   # 예금 금액
# abc.accountInfo()
#
# abc.withDraw(50000)
# abc.accountInfo()
# abc.printInterestRate()


class UserData(object):
    def __init__(self):
        self.year   = 2022
        self.month  = 2
        self.day    = 4

    def setYear(self, year):
        if year <= 0 :
            self.__year = 2022
        else :
            self.__year = year

    def getYear(self):
        return self.__year

myDate = UserData()
myDate.setYear(1900)
print(myDate.getYear())
print(myDate.month)
print(myDate.day)



class Super(object) :
    def __init__(self):
        pass
    def super_function(self):
        print('부모소유의 함수 슈퍼펑션~')
    def sayEcho(self,name):
        return name+'님 즐거운 하루 본내세요 ㅎㅎ'

class Sub(Super) :
    def __init__(self):
        pass

    def sub_function(self):
        print('본인 소유의 함수(자식)')

    def sayEcho(self,name):
        return name+'님 즐거운 코딩하세요~'

# 인스턴스 생성 구문
# 생성된 인스턴스의 주소값 입력하면 됨

child = Sub()
child.super_function()
child.sub_function()
print(child.sayEcho('정남선'))
print()
parent = Super()
parent.super_function()


class Unit() :
    def __init__(self, damage, life):
        self.utype  = self.__class__.__name__


class Order :
    def __init__(self, name):
        self.customer = 0
        self.name = name

    def order(self, price):
        self.customer += price
        return self.customer

class extraOrder(Order) :
    def order(self, price):
        self.customer += price
        return str(self.customer) + '원'

extraCustomer = extraOrder('영희')
print(extraCustomer.order(1000))