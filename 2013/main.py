
from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int) # Stores frequency of each point
        self.pts = [] # Stores all added points

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point # Extract query point coordinates
        for x, y in self.pts: # Loop through all stored points
            # Check if the point forms a diagonal with the query point
            if(abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            
            # Multiply occurrences of the two missing corners of the square
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res


# Running the code
detectSquares = DetectSquares()

# Add points
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])

print(detectSquares.count([11, 10]))  # Output: 1

