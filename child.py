from demo3 import Calculator


class ChildImpl(Calculator):

    num2 = 3

    def __init__(self):
        Calculator.__init__(self, 2, 4)

    def getCompleteData(self):
        return self.num2 + self.num +self.soma()

objt = ChildImpl()
print(objt.getCompleteData())