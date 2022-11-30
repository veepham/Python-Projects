
class Protected:
    def __init__(self):
        self._protectedVar = 0 # private attribute
        self.__privateVar = 4 # protected attribute
        
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected() # creating protected object
obj._protectedVar = 14
print(obj._protectedVar)

obj.getPrivate() # [ritvate object

