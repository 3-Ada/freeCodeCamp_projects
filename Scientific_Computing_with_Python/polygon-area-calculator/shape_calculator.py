

class Rectangle():
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            result = ''
            for i in range(self.height):
                result += '*'*self.width + '\n'
            return result

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def get_amount_inside(self, shape):
        return self.get_area()//shape.get_area()


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return 'Square(side={})'.format(self.width)

    def set_width(self, w):
        self.set_side(w)

    def set_height(self, h):
        self.set_side(h)
