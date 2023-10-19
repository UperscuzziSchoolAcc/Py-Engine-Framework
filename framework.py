import math
from random import randint as r

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
    
    __int__ = lambda self : Vector3(int(self.x), int(self.y), int(self.z))
    __float__ = lambda self : Vector3(float(self.x), float(self.y), float(self.z))
    __hex__ = lambda self : Vector3(hex(self.x), hex(self.y), hex(self.z))
    
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
    
    
    def setPos(self, v):
        if type(v) == Vector3:
            self.x = v.x
            self.y = v.y
            self.z = v.z
        elif type(v) in [int, float]:
            self.x = self.y = self.z = v
        else:
            raise Exception(f"Can only set to int, float, or Vector3. Not {type(v).__name__}")
    lerp = lambda self, a, n: Vector3((self.x + (a.x - self.x)) * n, (self.y + (a.y - self.y)) * n, (self.z + (a.z - self.z)) * n)
        
    magnitude = lambda self : (self.x * self.x + self.y * self.y + self.z * self.z)**.5    
    sqrMagnitude = lambda self : self.magnitude() * self.magnitude()
    def normalize(self):
        mag = self.magnitude()
        return (self.x / mag, self.y / mag, self.z / mag)
    
    down = lambda self : Vector3(0, -1, 0)
    up = lambda self : Vector3(0, 1, 0)
    forward = lambda self : Vector3(0, 0, 1)
    back = lambda self : Vector3(0, 0, -1)
    left = lambda self : Vector3(-1, 0, 0)
    right = lambda self : Vector3(1, 0, 0)
    zero = lambda self : Vector3(0, 0, 0)
    
    this = lambda self : [self.x, self.y, self.z]
    
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
        
    def fromHex(self, hex):
        if hex[0] == "#":
            self.r = int(hex[1:3], 16)
            self.g = int(hex[3:5], 16)
            self.b = int(hex[5:8], 16)
    
    def toHex(self, upper = True):
        rh = "{:02x}".format(self.r)
        gh = "{:02x}".format(self.g)
        bh = "{:02x}".format(self.b)
        if upper:
            return f"#{rh}{gh}{bh}".upper()
        else:
            return f"#{rh}{gh}{bh}"
    
    def fromEnum(self, color):
        color = color.lower()
        if color == "red":
            self.fromHex("#FF0000")
        elif color == "green":
            self.fromHex("#00FF00")
        elif color == "blue":
            self.fromHex("#0000FF")
        elif color == "white":
            self.fromHex("#FFFFFF")
        elif color == "black":
            self.fromHex("#000000")
        elif color == "pink":
            self.fromHex("#FFC0CB")
    
    def mono(self):
        a = (self.r + self.g + self.b)/3
        return Color(a, a, a)
        
    invserse = lambda self : Color(255 - self.r, 255 - self.g, 255 - self.b)
    random = lambda self : Color(r(0, 255), r(0, 255), r(0, 255))
        
    this = lambda self : [self.r, self.g, self.b]
    max = lambda self: max(max(self.r, self.g), self.b)
    min = lambda self: min(min(self.r, self.g), self.b)
