import pygame
import pygame.math as math
import random

from CODE.rectangle import Rectangle


class Quadtree:
    def __init__(self, boundary, capacity, max_depth=4, depth=0):
        self.boundary = boundary  # The rectangle boundary for this node
        self.capacity = capacity  # The maximum number of points before splitting
        self.max_depth = max_depth  # The maximum depth before stopping subdivision
        self.depth = depth  # The current depth of this node in the tree
        self.points = []  # List of points in this node
        self.divided = False  # Flag to check if the node has been subdivided
        self.northeast = None
        self.northwest = None
        self.southeast = None
        self.southwest = None

    def insert(self, point):
        """Insert a point into the quadtree. If the point lies within the boundary
           and the boundary is not subdivided, the point is added to the node. If the
           node is full, it will subdivide."""
        if not self.boundary.contains(point.pos):
            return False

        if len(self.points) < self.capacity or self.depth >= self.max_depth:
            self.points.append(point)
            return True

        if not self.divided:
            self.subdivide()

        if self.northeast.insert(point):
            return True
        if self.northwest.insert(point):
            return True
        if self.southeast.insert(point):
            return True
        if self.southwest.insert(point):
            return True

    def subdivide(self):
        """Subdivide the node into four quadrants only if necessary."""
        x = self.boundary.x
        y = self.boundary.y
        width = self.boundary.width
        height = self.boundary.height

        ne = Rectangle(x + width / 2, y + height / 2, width / 2, height / 2)
        nw = Rectangle(x, y + height / 2, width / 2, height / 2)
        se = Rectangle(x + width / 2, y, width / 2, height / 2)
        sw = Rectangle(x, y, width / 2, height / 2)

        self.northeast = Quadtree(ne, self.capacity, self.max_depth, self.depth + 1)
        self.northwest = Quadtree(nw, self.capacity, self.max_depth, self.depth + 1)
        self.southeast = Quadtree(se, self.capacity, self.max_depth, self.depth + 1)
        self.southwest = Quadtree(sw, self.capacity, self.max_depth, self.depth + 1)

        self.divided = True

        # Move all existing points to the correct quadrant
        for point in self.points:
            self.insert(point)

        self.points = []  # Clear points from the parent after inserting them into children

    def query(self, range, found=None):
        """Find all points that are within the specified range (another rectangle)."""
        if found is None:
            found = []

        if not self.boundary.intersects(range):
            return found

        for point in self.points:
            if range.contains(point.pos):
                found.append(point)

        if self.divided:
            self.northeast.query(range, found)
            self.northwest.query(range, found)
            self.southeast.query(range, found)
            self.southwest.query(range, found)

        return found

    def prune(self):
        """Remove empty subdivisions and reassign points back to the parent."""
        if self.divided:
            # Prune quadrants if they are empty
            if not self.northeast.points and not self.northwest.points and not self.southeast.points and not self.southwest.points:
                # If all child quadrants are empty, merge them back
                self.divided = False
                # Move points back to this node
                self.points.extend(self.northeast.points)
                self.points.extend(self.northwest.points)
                self.points.extend(self.southeast.points)
                self.points.extend(self.southwest.points)
                self.northeast = self.northwest = self.southeast = self.southwest = None

            # Recursively prune children
            if self.northeast:
                self.northeast.prune()
            if self.northwest:
                self.northwest.prune()
            if self.southeast:
                self.southeast.prune()
            if self.southwest:
                self.southwest.prune()

    def remove_empty_quadrants(self):
        """Removes quadrants that are empty and unnecessary."""
        if self.divided:
            # Check if all child quadrants are empty
            if not self.northeast.points and not self.northwest.points and not self.southeast.points and not self.southwest.points:
                self.divided = False
                self.northeast = self.northwest = self.southeast = self.southwest = None

            # Recursively check children
            if self.northeast:
                self.northeast.remove_empty_quadrants()
            if self.northwest:
                self.northwest.remove_empty_quadrants()
            if self.southeast:
                self.southeast.remove_empty_quadrants()
            if self.southwest:
                self.southwest.remove_empty_quadrants()
