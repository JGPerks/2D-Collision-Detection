class Rectangle:
    """Represents a rectangle boundary with x, y for the bottom-left corner,
       and width and height for the rectangle dimensions."""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, point):
        """Check if the point (x, y) is within the rectangle."""
        return (self.x <= point.x < self.x + self.width) and (self.y <= point.y < self.y + self.height)

    def intersects(self, range):
        """Check if the rectangle intersects with another rectangle."""
        return not (range.x + range.width <= self.x or
                    range.x >= self.x + self.width or
                    range.y + range.height <= self.y or
                    range.y >= self.y + self.height)