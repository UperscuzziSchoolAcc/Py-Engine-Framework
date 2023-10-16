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
    
    def __div__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x / a.x, self.y / a.y, self.z / a.z)
        else:
            return Vector3(self.x / a, self.y / a, self.z / a)
            
    def __floordiv__(self, a):
        if type(a) == Vector3:
            return Vector3(self.x // a.x, self.y // a.y, self.z // a.z)
        else:
            return Vector3(self.x // a, self.y // a, self.z // a)
        
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
        
    def lerp(self, a, n):
        return a +
        
    back = lambda self : Vector3(0, 0, -1)
        
    down = lambda self : Vector3(0, -1, 0)
        
    forward = lambda self : Vector3(0, 0, 1)
        
    left = lambda self : Vector3(-1, 0, 0)

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

a = Vector3(5, 6, 7)
b = Vector3(1, 4, 5)

print(a % b)
print(a >= b)