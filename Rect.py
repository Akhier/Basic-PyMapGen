class Rect:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Height = 0
        self.Width = 0

    @classmethod
    def create_new(r, x, y, width, height):
        newRect = r()
        newRect.set_loc(x,y)
        newRect.Height = height
        newRect.Width = width
        return newRect

    @classmethod
    def create_area(r, width, height):
        newRect = r()
        newRect.Height = height
        newRect.Width = width
        return newRect

    def set_loc(self, x, y):
        self.X = x
        self.Y = y

    def is_edge(self, x, y):
        if x == self.X or x == self.X + self.Width - 1:
            if y < self.Y + self.Height and y >= self.Y:
                return True
            else:
                return False

        elif y == self.Y or y == self.Y + self.Height - 1:
            if x < self.X + self.Width and x >= self.X:
                return True
            else:
                return False

        else:
            return False

    def is_inside(self, x, y):
        if x >= self.X and x <= self.farX() and y >= self.Y and y <= self.farY():
            return True
        else:
            return False

    def farX(self):
        return self.X + self.Width - 1

    def farY(self):
        return self.Y + self.Height - 1

if __name__ == '__main__':
    test = Rect.create_new(5, 6, 7, 8)
    test2 = Rect.create_new(1, 1, 1, 1)
    print(test.X)
    print(test.Y)
    print(test.Height)
    print(test.Width)
    print(test.is_edge(5, 7))
    print(test.is_edge(5, 5))
    print(test.is_edge(6, 6))
    print(test.is_edge(4, 6))
    print(test.is_edge(4, 5))