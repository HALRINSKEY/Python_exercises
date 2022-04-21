class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return (self.width * 2) + (self.len * 2)

class Square(Shape):
    def __init__(self,l):
        self.len = l

    def change_size(self,l):
        self.len += l

    def calculate_perimeter(self):
        return self.len * 4



a_rectangle = Rectangle(2,4)
a_square = Square(4)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

a_square.change_size(-2)
print(a_square.calculate_perimeter())

a_rectangle.what_am_i()

#()をつけないと実行されないので注意　a_rectangle.what_am_i() ←
