
'''
Exception - xxxxerror 모든에러 처리
예외처리 구문
try      :
    예외가 발생할 가능성이 있는 코드를 정의하는 곳
    A
    B
except A :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
except B :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
else     :
    예외가 발생되지 않을 때 실행되는 곳
finally  :
    예외발생 여부와 상관없이 실행되는 곳
'''

#function define - worker
def smpInput() :
    try :
        age = int(input('나이를 입력하세요 :    '))
    except ValueError as e :
        smpInput()
    else :
        print('당신의 나이는 ' , age , '입니다.')
    finally:
        print("무조건 출력~")


# caller
#smpInput()

'''
매개변수로 넘겨받은 각 첨자번지의 값에 제곱한 결과를
출력하려고 한다.
예외 발생을 확인하고 예외처리 구문을 추가하여 
정상적인 흐름의 함수 호출이 되도록 만들어 본다면?
'''

def exceptionFunc(lst) :

    for e in lst :
        try :
            print('raw - : ' , e)
            sqrt = e ** 2
            print('squared - ' , sqrt)
        except TypeError as e :
            pass

usrlst = [10, 20 , 25, 'num' , 40, 50]
#exceptionFunc(usrlst)


# 사용자 정의 예외 클래스

class UserNegativeDivisionError(Exception) :
    def __init__(self, msg):
        self.msg = msg

def positiveDivide(x,y) :
    if (y < 0 ):
       raise UserNegativeDivisionError('음수로 나눌 수 없습니다.')
    else :
        return x/y

try :
    result = positiveDivide(10, -2)
    print(result)
except UserNegativeDivisionError as e :
    print(e.msg)
except ZeroDivisionError as e :
    print(e)


class MagicClass(object) :
    def __init__(self):
        print('객체 생성시 호출')
    def __del__(self):
        print('객체 삭제시 호출')
    def __str__(self):
        return '주소값이 아니라 문자열이 출력'

obj = MagicClass() #
print(obj.__str__())
