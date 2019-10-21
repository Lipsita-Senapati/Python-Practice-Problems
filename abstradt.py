from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(Shape):
     def area(self):
            l=10
            b=5
            print(l*b)

class circle(Shape):
     def area(self):
            r=5
            print(3.14*r*r)
class triangle(Shape):
    def area(self):
        b=5
        h=8
        print(0.5*b*h)
        

r=rectangle()
c=circle()
t=triangle()
t.area()
r.area()
c.area()


    
