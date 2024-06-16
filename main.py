import math
#Zadanie 1
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return (f'{self.title} {self.author, self.year} - {self.genre}')

    def age(self):
        print(2024 - self.year)

    def __repr__(self):
        return (f'{self.title} {self.author, self.year} - {self.genre}. Был вызван __repr__')


b1 = Book('Капитнаская дочка', 'A. Пушкин', 1836, 'Historical novel')
b1.__str__()
b1.__repr__()
b1.age()
print(repr(b1))



#Zadanie 2
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    def add_grade(self, grade):
        self.grades.append(grade)
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    def __str__(self):
        print(f'Name: {self.name}, Age: {self.age}, Average Grade: {self.average_grade()}')
vasya_grades = [4,5,3,5,4]
vasya = Student('Vasya', 15, vasya_grades)
vasya.__str__()
vasya_average = vasya.average_grade()
vasya.add_grade(5)
vasya_average_2 = vasya.average_grade()
print(vasya_average)
print(vasya_average_2)



#Zadanie 3
class Shape:
    def __init__(self):
        self.name = ''
    def area(self):
         return self
    def perimeter(self):
        return 2 * self
# с классом Shape я не разобрался поэтому вписал просто слова которые предлагает PyCharm
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(math.pi * self.radius ** 2)
    def perimeter(self):
        print(2 * math.pi * self.radius)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print(self.width * self.height)
    def perimeter(self):
        print((self.width + self.height) * 2)
class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
circle = Circle(5)
rectangle = Rectangle(5,4)
square = Square(3)
circle.area()
circle.perimeter()
rectangle.area()
rectangle.perimeter()
square.area()
square.perimeter()



