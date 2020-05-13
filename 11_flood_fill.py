class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        def dfs(r, c):
            
            if image[r][c] == color:
                image[r][c] = newColor
                
                if r >= 1: #top
                    dfs(r-1, c)
                    
                if r+1 < row: #bottom
                    dfs(r+1, c)
                    
                if c >= 1: #left
                    dfs(r, c-1)
                    
                if c+1 < col: #right
                    dfs(r, c+1)
        
        dfs(sr,sc)
        
        return image