class point: 
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
        
    
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.lt = point(x1,y1)
        self.rb = point(x2,y2)

    
    def show(self):
        print(f'좌측 상단의 꼭지점이 ({self.lt.x},{self.lt.y})이고',end='')
        print(f'우측 상단의 꼭지점이 ({self.rb.x},{self.rb.y})인 사각형 입니다.')

    def getwidth(self):
        return self.rb.x - self.lt.x
    
    def getheight(self):
        return self.rb.y - self.lt.y
    
    def getarea(self):
        return self.getwidth() * self.getheight()
    
    def getperimeter(self):
        return 2*(self.getheight() + self.getwidth())


r1 = Rectangle(5,5,20,10)
a = r1.getarea()
p = r1.getperimeter()
r1.show()
print(f'넓이는 {a}, 둘레는 {p}')