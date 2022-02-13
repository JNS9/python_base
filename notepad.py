
class FourCal :
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
#a.setdata(4, 2)
b = FourCal(3, 7)
#b.setdata(3,7)

print(a.first)
print(b.first)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

class MoreFourCal(FourCal) :
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(3, 4)
print(a.add())
print(a.pow())

class SafeFourCal(FourCal) :
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

a = SafeFourCal(4 , 0)
print(a.div())


class Family :
    lastname = "상"

print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)


def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

