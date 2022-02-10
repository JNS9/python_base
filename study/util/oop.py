class Person :
    # initailizer(magic function) __로 시작해서 __로 끝나는 애들
    # 객체 생성시 자동으로 호출되는 함수
    # 명시적으로 호출이 불가능하다.
    def __init__(self, name, subject, email):   #이게 인스턴스?
        self.name       = name      # self를 붙여 인스턴스 소유의 변수로 지정
        self.subject    = subject   # self를 없애면 인스턴스 소유가 아니게된다.
        self.email      = email

    def perInfo(self):
        return '이름 {} , 과목 {} , 메일 {}'.format(self.name , self.subject , self.email)
