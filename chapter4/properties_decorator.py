class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        """rectangle width measured from left"""
        return self.x2 - self.x1

    @width.setter
    def width(self, value):
        self.x2 = self.x1 + value

    @property
    def height(self):
        """rectangle height measured from top"""
        return self.y2 - self.y1

    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value


if __name__ == "__main__":
    rectangle = Rectangle(0, 0, 10, 10)
    print(
        f"At start we have {rectangle} with "
        f"size of {rectangle.width} x {rectangle.height}"
    )

    rectangle.width = 2
    rectangle.height = 8
    print(
        f"After resizing we have {rectangle} with "
        f"size of {rectangle.width} x {rectangle.height}"
    )
