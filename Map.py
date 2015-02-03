from Rect import Rect

class Map:
    def __init__(self, width, height):
        self.Height = height
        self.Width = width
        self._tiles = [[0 for y in range(self.Height)] for x in range(self.Width)]

    def set_tile(self, id, x, y):
        self._tiles[y][x] = id

    def get_tile(self, x, y):
        return self._tiles[y][x]

    def set_area(self, id, r):
        for y in  range(0, r.Height - 1):
            for x in range(0, r.Width - 1):
                self.set_tile(id, r.X + x, r.Y + y)

    def set_edge(self, id, r):
        for y in range(r.Y, r.Y + r.Height):
            for x in range(r.X, r.X + r.Width):
                if r.is_edge(x, y):
                    self.set_tile(id, x, y)

if __name__ == '__main__':
    test = Map(9, 12)
    x = 0
    y = 1
    test.set_tile(2, x, y)
    print (test.get_tile(x, y))
    x2 = 2
    y2 = 3
    h = 4
    w = 5
    test.set_area(3, Rect.create_new(x2, y2, w, h))
    test.set_edge(4, Rect.create_new(x2, y2, w, h))
    print (test._tiles)