class Expression:
    def __str__(self):
        return self.str_aux(0)

"""Representation of a simple variable"""
class Var(Expression):
    def __init__(self, name):
        self.name = name

    def str_aux(self, prec):
        return self.name

    def eval(self, env):
        return env[self.name]

"""Representation of a simple constant (i.e. a number)"""
class Const(Expression):
    def __init__(self, val):
        self.val = val    

    def str_aux(self, prec):
        return str(self.val)

    def eval(self, env):
        return self.val
    

"""Representation of a generic binary operation"""
class BinOp(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def str_aux(self, prec):
        s = self.left.str_aux(self.prec) + str(self.symbol) + self.right.str_aux(self.prec)
        if self.prec < prec:
            return "(" + s + ")"
        else:
            return s
    
    def eval (self, env):
        print("Calling eval")
        return self.fun(self.left.eval(env), self.right.eval(env))

"""Representation of a 'Times' operation"""
class Times(BinOp): 
    symbol = "*"
    prec = 2

    def fun(self, x, y):
        return x*y

"""Representation of a 'Plus' operation"""
class Plus(BinOp):
    symbol = "+"
    prec = 1   

    def fun(self, x, y):
        return x+y 

#(x+z) *(y+(x+y))
expr1 = Times(Plus(Var('x'), Var('z')), Plus(Var('y'), Plus(Var('x'), Var('y'))))
env = {'x':2, 'y':3, 'z':4}
print(expr1.eval(env))