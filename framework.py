import math

inf = float("inf")

def clamp(n, nmin, nmax): 
    if n < nmin: 
        return nmin
    elif n > nmax: 
        return nmax
    else: 
        return n

class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    __call__ = lambda self : (self.x, self.y, self.z)
    
    def __add__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x + a.x, self.y + a.y, self.z + a.z)
        else:
            return Vector3(self.x + a, self.y + a, self.z + a)
        
    def __sub__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x - a.x, self.y - a.y, self.z - a.z)
        else:
            return Vector3(self.x - a, self.y - a, self.z - a)
    
    def __mul__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x * a.x, self.y * a.y, self.z * a.z)
        else:
            return Vector3(self.x * a, self.y * a, self.z * a)
    
    def __truediv__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x / a.x, self.y / a.y, self.z / a.z)
        else:
            return Vector3(self.x / a, self.y / a, self.z / a)
            
    def __floordiv__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x // a.x, self.y // a.y, self.z // a.z)
        else:
            return Vector3(self.x // a, self.y // a, self.z // a)
            
    def __pow__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x ** a.x, self.y ** a.y, self.z ** a.z)
        else:
            return Vector3(self.x ** a, self.y ** a, self.z ** a)
            
    def __eq__(self, a):
        if type(a) == Vector3:
            return a.x == self.x and a.y == self.y and a.z == self.z
        else:
            return a == self.x and a == self.y and z == self.z
            
    def __ne__(self, a):
        if type(a) == Vector3:
            return a.x != self.x and a.y != self.y and a.z != self.z
        else:
            return a != self.x and a != self.y and z != self.z
        
    def __mod__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x % a.x, self.y % a.y, self.z % a.z)
        else:
            return Vector3(self.x % a, self.y % a, self.z % a)
        
    def __ge__(self, a): 
        if type(a) == Vector3:
            return (self.x * self.x + self.y * self.y + self.z * self.z)*.5 >= (a.x * a.x + a.y * a.y + a.z * a.z)*.5
        else:
            return (self.x * self.x + self.y * self.y + self.z * self.z)*.5 >= a
        
    __str__ = lambda self: f'{self.x} {self.y} {self.z}'
        
    __neg__ = lambda self: Vector3(-self.x, -self.y, -self.z)
        
    max = lambda self: max(max(self.x, self.y), self.z)
    min = lambda self: min(min(self.x, self.y), self.z)
    
    lerp = lambda self, a, n: Vector3((self.x + (a.x - self.x)) * n, (self.y + (a.y - self.y)) * n, (self.z + (a.z - self.z)) * n)
        
    down = lambda self : Vector3(0, -1, 0)
    up = lambda self : Vector3(0, 1, 0)
    forward = lambda self : Vector3(0, 0, 1)
    back = lambda self : Vector3(0, 0, -1)
    left = lambda self : Vector3(-1, 0, 0)
    right = lambda self : Vector3(1, 0, 0)
    zero = lambda self : Vector3(0, 0, 0)
    
    negativeInfinity = lambda self : Vector3(-inf, -inf, -inf)
    positiveInfinity = lambda self : Vector3(inf, inf, inf)
    
    __repr__ = lambda self : f"X: {self.x}\nY: {self.y}\nZ: {self.z}"

class Color:
    def __init__(self, r = 255, g = 255, b = 255):
        self.r = r
        self.g = g
        self.b = b
        
    def __call__(self):
        return (self.r, self.g, self.b)
        
    def setColorFromDecimal(self, r, g, b):
        self.r = clamp(round(255 * r), 0, 255)
        self.g = clamp(round(255 * g), 0, 255)
        self.b = clamp(round(255 * b), 0, 255)
