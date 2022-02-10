'''
[실습]
- 1. Account class 작성
- 2. 인스턴스 변수 - type(S|F), account, balance, interestRate
- 2-1 SavingAccount(Account), FundAccount(Account)
- 3. accountInfo() - 계좌 정보를 출력하는 함수
- 4. deposit(amount) - 매개변수 들어온 amount를 balance 입금
- 5. withDraw(amount) - 매개변수 들어온 amount를 balance 출금
- 5-1. 단) 잔고가 부족할 경우 ' 잔액이 부족하여 출금이 안돼요'
- 6. printInterestRage() - 현재 잔액에 이자율을 계산하여 소수점 2자리까지 출력

- 2-1. SavingAccount(Account), FundAccount(Account)
        overriding  -- printInterestRate()
-- SavingAccount -printInterestRate()
    기본 이자율에 만기시 이자율을(0.1) 계산
-- FundAccount -printInterestRate()
    기본 이자율에 잔액이 10만원 이상이면 10%
    기본 이자율에 잔액이 50만원 이상이면 15%
    기본 이자율에 잔액이 100만원 이상이면 20%
'''

class Account(object) :
    pass
class SavingAccount(Account) :
    pass
class FundAccount(Account) :
    pass

# caller
