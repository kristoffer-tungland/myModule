from _mySubBase import _MySubBase

class MySubClass (_MySubBase):
    def __init__(self, baseParameter, parameter):
        super(MySubClass, self).__init__(baseParameter)
        self.parameter = parameter

    def classFunction(self):
        print('classFunction called')