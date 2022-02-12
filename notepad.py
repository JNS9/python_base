
class FourCal :
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


a = FourCal()
a.setdata(4, 2)
b = FourCal()
b.setdata(3,7)

print(a.first)
print(b.first)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

