class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 2:
            return True
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        y = (y1 - y0)
        x = (x1 - x0)
        
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            
            if y * (xi - x0) != (yi - y0) * x:
                return False
            
        return True