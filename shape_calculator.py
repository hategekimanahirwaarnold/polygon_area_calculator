import math

class Rectangle:
    def __init__(self, width, height):
        if width <= height:
            self.width = width
            self.height = height
        else: 
            self.width = height
            self.height = width
    
    def set_width(self, width):
        if self.width == self.height:
            self.width = width
            self.height = width
        else:
            self.width = width
    
    def set_height(self, height):
        if self.width == self.height:
            self.width = height
            self.height = height
        else:
            self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            string = ""
            for y in range(self.height):
                for x in range(self.width):
                    string += "*"
                string += "\n"
            return string
    
    def get_amount_inside(self, otherShape):
        return math.floor(self.get_area() / otherShape.get_area())

    def __str__(self):
        if self.width == self.height:
            return f"Square(side={self.width})"
        else: 
            return f"Rectangle(width={self.width}, height={self.height})"
    



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) #Call Rectangle's constructor

    def set_side(self, side):
        self.width = side
        self.height = side

