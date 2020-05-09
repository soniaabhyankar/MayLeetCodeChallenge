class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        low = 2
        high = num
        
        while low <= high:
            mid = (low + high) // 2
            sqr = mid**2
            
            if sqr == num:
                return True
            
            elif sqr > num:
                high = mid - 1
                
            else:
                low = mid + 1
                
        return False