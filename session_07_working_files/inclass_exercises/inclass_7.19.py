# 7.19:  Allow an object to respond to subscripting.  Define a
# __setitem__(self) method that takes two arguments (besides
# self) and prints the two arguments.  Now attempt to
# subscript the object.

class Value:
    def __init__(self, val):
        self.aaa = val

    def getval(self):
        return self.aaa

mynum = Value('10')

mynum['a'] = 55



