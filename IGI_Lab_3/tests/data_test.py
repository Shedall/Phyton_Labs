import math

x = 10   
def my_func(a):
    str = "test_func"
    le = len(str)
    print(str," ",le)
    return math.sin(a + x)

def my_func_2(*args):
    sum = 0

    for n in args:
        sum += n

    print("Sum: ", sum)
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("func start")
        res = func(*args, **kwargs)
        print("Func end")
        return res
        
    return wrapper

#@my_decorator
def for_dec(a):
    print("Hello World!", a)
    
X = 12
class A:
    bob = "sinii"
    
    
    @staticmethod
    def ret_bob():
        return A.bob

    @classmethod
    def ret_boby(cls):
        return cls.bob
    
    def my_method(self, x):
        return x + 5

class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hi:)")
        return math.sin(k * X)

class C(A, B):
    def __init__(self):   
        self.coca = "Cola"
        
    def abobus(self, k):
        return k
    #создать объект класса С и серилизовать методы из класса А