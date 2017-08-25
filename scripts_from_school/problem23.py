'''Thomas Whitzer 159005085'''

import math

class StraightLine:

    def __init__(self, a = 0, b = 0, c = 0):
        
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):

        line = ''

        if self.a != 0:
            if self.b < 0:
                line += str(self.a) + 'x' + ' - ' + str(abs(self.b)) + 'y' + ' = ' + str(self.c)
                return line
            elif self.b == 0:
                line += str(self.a) + 'x' + ' = ' + str(self.c)
                return line
            else:
                line += str(self.a) + 'x' + ' + ' + str(self.b) + 'y' + ' = ' + str(self.c)
                return line
        else:
                line += str(self.a) + 'x' + ' + ' + str(self.b) + 'y' + ' = ' + str(self.c)
                return line

    def __repr__(self):

        return '%sclass StraighLine object: %s%s' % ('<', self, '>')
        

    def slope(self):

        if self.b == 0:
            #print('Undefined (Line is vertical)')
            return None
        elif self.a == 0:
            m = 0.00
            #print(m)
            return m
        else:
            if self.a < 0:
                m = self.a / self.b
                #print('%.2f' % m)
                return m
            else:
                m = -self.a / self.b
                #print('%.2f' % m)
                return m

    def yintercept(self):

        if self.b == 0:
            #print('Undefined (Line is vertical)')
            return None
        else:
            yint = self.c / self.b
            #print('%.2f' % yint)
            return yint

    def xintercept(self):

        if self.a == 0:
            #print('Undefined (Line is horizontal)')
            return None
        else:
            xint = self.c / self.a
            #print('%.2f' % xint)
            return xint
        
    def parallel(self, L):
        '''
        returns True if self and L are parallel and False otherwise
        '''
        
        a = self.slope()
        b = L.slope()
        
        if a == b:
            #print(True)
            return True
        else:
            #print(False)
            return False
        
    def perpendicular(self, L):

        '''
        returns True if self and L are perpendicular and Falase otherwise
        '''

        a = self.slope()
        b = L.slope()

        if self.parallel(L) == True:
            print(False)
            return False
        else:
            if a != None and b != None:
                if a * b == 1.0:
                    print(True)
                    return True
                elif a == None and b == 0.0:
                    print(True)
                    return True
                elif a == 0.0 and b == None:
                    print(True)
                    return True
                else:
                    print(False)
                    return False
            elif a == None and b == 0.0:
                print(True)
                return True
            elif a == 0.0 and b == None:
                print(True)
                return True
            else:
                print(False)
                return False

    def intersection(self, L):

        x1 = self.slope()
        y = self.b
        c = self.yintercept()
        x2 = L.slope()
        y2 = L.b
        c2 = L.yintercept()

        if self.parallel(L) == True:
            return None
        else: 

            b = c2 - c
            m = x1 - x2
            x = b/m
            y1 = x1 * x + c
            y2 = x2 * x + c2
            
            return (x, y1)
            
            
            

    def __eq__(self, another_point):

        a_slope = self.slope()
        a_yint = self.yintercept()

        b_slope = another_point.slope()
        b_yint = another_point.yintercept()
        
        if a_slope == b_slope and a_yint == b_yint:
            return True
        else:
            return False

    def __ne__(self, another_point):

        a_slope = self.slope()
        a_yint = self.yintercept()

        b_slope = another_point.slope()
        b_yint = another_point.yintercept()
        
        if a_slope == b_slope and a_yint == b_yint:
            return False
        else:
            return True
        
            
I = StraightLine(1, 2, -3)
P = StraightLine(-2, 1, 3)
S = StraightLine(2, 5, 4)
C = StraightLine(1, 2, -3)
X = StraightLine()

#I.perpendicular(P)
