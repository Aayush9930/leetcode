# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            if sea.hasShips(topRight, bottomLeft) == True:
                return 1
            return 0
        if not sea.hasShips(topRight, bottomLeft):
                return 0

        
        mid_x = (topRight.x + bottomLeft.x) // 2 
        mid_y = (topRight.y + bottomLeft.y) // 2 

        topRQ = self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
        topLQ = self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
        bottomLQ = self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
        bottomRQ = self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))

        return topLQ + topRQ + bottomLQ + bottomRQ




        
