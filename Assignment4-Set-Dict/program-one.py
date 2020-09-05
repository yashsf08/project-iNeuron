"""

    1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
        formula.
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    Function to take the length of the sides of triangle from user should be defined in the parent
    class and function to calculate the area should be defined in subclass
"""

class Shape(object):
    
    def get_len(self,a):
        self.a,self.b,self.c = int(a[0]),int(a[1]),int(a[2])
        
class Area(Shape):
    def calculate(self):
        s = (self.a+self.b+self.c)/2
        print('Area of the triangle is : ',(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5)


obj = Area()
obj.get_len(input('Hello User please provide length of 3 side of the triangle: ').split())
obj.calculate()


"""

    1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
        the list of words that are longer than n.

"""

def filter_long_words(words, n):
    if(n):
        result = [i for i in words if len(i)>n]
        return result

    else:
        return None


print(filter_long_words(input('Dear user, please provide list of wordsn :  ').split(), 3))