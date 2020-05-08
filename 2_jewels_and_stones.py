class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        
        for x in J:
            jewels += S.count(x)
            
        return jewels