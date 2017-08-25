'''Thomas Whitzer 159005085'''

class Container:

    def __init__(self, contents = []):

        '''
        initalizes  self.contents
        '''

        self.contents = contents

        
    
    def insert(self, item):

        '''
        appends item to self.contents
        '''

        self.contents.append(item)
        return self.contents

    def erase_one(self, item):

        '''
        erases one occurrance of item in self.contents
        '''

        for i in self.contents:
            if i == item:
                self.contents.remove(i)
                return self.contents
            else:
                continue

    def erase_all(self, item):

        '''
        erases all occurrances of item in self.contents
        '''

        self.contents = [x for x in self.contents if x != item]
        return self.contents

    def count(self, item):

        '''
        counts the number of times item appears in self.contents
        '''

        counter = 0

        for i in self.contents:
            if i == item:
                counter += 1
            else:
                continue
        return counter

    def items(self):

        '''
        returns all elements in self.contents
        '''

        L = []

        for i in self.contents:
            if i in L:
                continue
            else:
                L.append(i)
        return L

    def __str__(self):   

        '''
        overloads print: self.contents ordered
        '''
        
        S1 = []
        S2 = []
        In1 = []
        In2 = []
        F1 = []
        F2 = []
        Lstr_1 = []
        Lstr_2 = []
        Lint_1 = []
        Lint_2 = []
        Lfloat_1 =[]
        Lfloat_2 = []

        '''
        seperates elements in self.contents into lists of the same type
        '''
        for i in self.contents:
            if type(i) == str:
                S1.append(i)
            elif type(i) == int:
                In1.append(i)
            elif type(i) == float:
                F1.append(i)
            elif type(i) == list and type(i[0]) == str:
                Lstr_1.append(i)
            elif type(i) == list and type(i[0]) == int:
                Lint_1.append(i)
            elif type(i) == list and type(i[0]) == float:
                Lfloat_1.append(i)

        '''
        sorts type lists
        '''
        for i in sorted(S1):
            S2.append(i)
        for i in sorted(In1):
            In2.append(i)
        for i in sorted(F1):
            F2.append(i)
        for i in sorted(Lstr_1): 
            Lstr_2.append(i)
        for i in sorted(Lint_1):
            Lint_2.append(i)
        for i in sorted(Lfloat_1):
            Lfloat_2.append(i)
        self.contents = []

        '''
        appends seperate type lists back into self.contents in the correct order
        '''

        counter = 0
        
        while counter != 6:
            #self.contents.append(In2)
            if len(In2) > 0 and counter < 1:
                for i in In2:
                    self.contents.append(i)
                counter += 1
            elif len(In2) == 0 and counter < 1:
                counter += 1
        #self.contents.append(F2)
            elif len(F2) > 0 and counter < 2:
                for i in F2:
                    self.contents.append(i)
                counter += 1
            elif len(F2) == 0 and counter < 2:
                counter += 1

            #self.contents.append(S2)
            elif len(S2) > 0 and counter < 3:
                for i in S2:
                    self.contents.append(i)
                counter += 1
            elif len(S2) == 0 and counter < 3:
                counter += 1
                
            #self.contents.append(L2)
            elif len(Lstr_2) > 0 and counter < 4:
                for i in Lstr_2:
                    self.contents.append(i)
                counter += 1
            elif len(Lstr_2) == 0 and counter < 4:
                counter += 1

            elif len(Lint_2) > 0 and counter < 5:
                for i in Lint_2:
                    self.contents.append(i)
                counter += 1
            elif len(Lint_2) == 0 and counter < 5:
                counter += 1

            elif len(Lfloat_2) > 0 and counter < 6:
                for i in Lfloat_2:
                    self.contents.append(i)
                counter += 1
            elif len(Lfloat_2) == 0 and counter < 6:
                counter += 1
        
        return str(self.contents)

    def __repr__(self):

        return '<Container object>'

        

    def __add__(self, anotherContainer):

        '''
        overloading + : returns new container of all items in self and anotherContainer
        '''

        a = self.contents
        b = anotherContainer.items()
        NewContainer = Container()
        n = NewContainer.items()

        for i in a:
            n.append(i)

        for i in b:
            n.append(i)
        NewContainer = Container(n)
        return NewContainer

    def __sub__(self, anotherContainer):

        '''
        overloading - : returns new Container of self minus items that occur in
                        anotherContainer
        '''

        n = self.contents
        subItems = anotherContainer.items()
        NewContainer = Container()

        for i in n:
            if i in subItems:
                n.remove(i)
            else:
                continue

        NewContainer = Container(n)
        return NewContainer

    def __mul__(self, anotherContainer):

        '''
        overloading * : returns new Container with items that occur in self.contents
                        and anotherContainer
        '''

        a = self.contents
        b = anotherContainer.items()
        NewContainer = Container()
        n = NewContainer.items()

        for i in a:
            if i in b:
                if i in n:
                    continue
                else:
                    n.append(i)
            else:
                continue
        NewContainer = Container(n)
        return NewContainer
    
    

I = Container([1, 2, "abc", 2, [4]])
P = Container([3, 2, 4, "abcd", [4], "xy"])

