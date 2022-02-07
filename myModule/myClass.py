from _myBase import _MyBase

class MyClass (_MyBase):
    def __init__(self, baseParameter, parameter):
        super(MyClass, self).__init__(baseParameter)
        self.parameter = parameter

    def classFunction(self):
        print('classFunction called')