class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        intervals = []
        
        while a < len(A) and b < len(B):
            
            starting, ending = max(A[a][0], B[b][0]), min(A[a][1], B[b][1])
            
            if starting <= ending:
                intervals.append([starting, ending])
            
            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1
        
        return intervals