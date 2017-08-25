'''Thomas Whitzer 159005085'''


import math

class Point:

    def __init__(self, x = 0, y=0):
        self.x = x
        self.y = y

    def translate(self, s, t):
        self.x += s
        self.y += t

    def rotate(self, angle):
        x = self.x
        angle = math.radians(angle)
        self.x = (x * math.cos(angle)) - (self.y * math.sin(angle))
        self.y = (x * math.sin(angle)) + (self.y * math.cos(angle))

    def distance(self, p):
        distance = (self.x - p.x)**2 + (self.y - p.y)**2
        distance = math.sqrt(distance)
        return distance

    def left_of(self, q, r):
        return (((r.x * self.y - self.x * r.y) + (q.x * r.y - q.x * self.y) + (q.y * self.x - q.y * r.x)) > 0)

    def right_of(self, q, r):
        return (((r.x * self.y - self.x * r.y) + (q.x * r.y - q.x * self.y) + (q.y * self.x - q.y * r.x)) < 0)

    def __str__(self):
        return'({0}, {1})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)

class SimplePoly:

    def __init__(self, *vertices):
        self.poly = [v for v in vertices]
        self.idx = 0

    def translate(self, s, t):
        for el in self.poly:
            el.translate(s,t)

    def rotate(self, angle): 
        for el in self.poly: 
            el.rotate(angle)

    def __iter__(self):
        return self

    def __next__(self):
        
        stop = len(self.poly)
        if self.idx <= stop:
            i = self.poly[self.idx]
            self.idx += 1
            return i
        else:
            raise StopIteration

    def __len__(self): 
        return len(self.poly)

    def __getitem__(self, i):
        if i > len(self.poly) or i < 0:
            IndexError
        else:
            return self.poly[i]

    def __str__(self):
        return str(self.poly)

    def __repr__(self):
        x = str(self)
        return x

    def perimeter(self):
        perim = 0
        for el in range(len(self.poly) - 1):
            if el == len(self.poly):
                perim += self.poly[el].distance(self.poly[0])
            else:
                perim += self.poly[el].distance(self.poly[el + 1])
        return perim

class ConvPoly(SimplePoly):

    def __init__(self, *vertices):
        templist = [v for v in vertices]
        for el in range(len(templist)):
            if (el + 2) >= len(templist):
                if (el+1) >= len(templist):
                    if templist[el].left_of(templist[0], templist[1]) == False:
                        Exception ('This is not a Convex Poly')
                elif templist[el].left_of(templist[el+1], templist[0]) == False:
                    Exception ('This is not a Convex Poly')
            elif templist[el].left_of(templist[el+1], templist[el+2]) == False:
                Exception ('This is not a Convex Poly')
        return super().__init__(*vertices)
        
class EquiTriangle(ConvPoly):

    def __init__(self, length):
        self.length = length
        a = Point(0,0)
        b = Point(length, 0)
        c = Point((length/2),(length *(math.sqrt(3)/2)))
        vertices = [c, a, b]
        self.tri = vertices
        return super().__init__(c,a,b)

    def area(self):
        a = self.tri[0].distance(self.tri[1])
        A = ((math.sqrt(3)/4) * (a**2))
        return A

class Rectangle(ConvPoly):

        def __init__(self, length, width):
            self.length = length
            self.width = width
            a = Point(0,0)
            b = Point(length,0)
            c = Point(length, width)
            d = Point(0, width)
            vertices = [a,b,c,d]
            self.rec = vertices
            return super().__init__(a,b,c,d)

        def area(self):
            a =  self.length * self.width
            return a

class Square(Rectangle):

    def __init__(self, length):
        a = Point(0,0)
        b = Point(length, 0)
        c = Point(length, length)
        d = Point(0, length)
        vertices = [a,b,c,d]
        self.square = vertices
        return super().__init__(length, length)


        
