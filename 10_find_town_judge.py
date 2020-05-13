class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if len(trust) < N-1:
            return -1
        
        trust_scores = [0] * (N+1)
        
        for out_, in_ in trust:
            trust_scores[out-] -= 1
            trust_score[in_] += 1
            
        for i, score in enumerate(trust_scores[1:], 1):
            if score == N - 1:
                return i
        
        return -1