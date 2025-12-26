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
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1 if sea.hasShips(topRight, bottomLeft) == True else 0 
        elif topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0 
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        midx = (topRight.x + bottomLeft.x) // 2 
        midy = (topRight.y + bottomLeft.y) // 2 

        ul = self.countShips(sea, Point(midx, topRight.y), Point(bottomLeft.x, midy + 1))
        ur = self.countShips(sea, topRight, Point(midx + 1, midy + 1))
        ll = self.countShips(sea, Point(midx, midy), bottomLeft)
        lr = self.countShips(sea, Point(topRight.x, midy), Point(midx + 1, bottomLeft.y))

        return ul + ur + ll + lr




























