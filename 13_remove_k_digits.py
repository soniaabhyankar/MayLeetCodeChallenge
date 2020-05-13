class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        digits_to_remove = k
        
        for current in num:
            while digits_to_remove and stack and stack[-1] > current:
                stack.pop()
                digits_to_remove -= 1
            stack.append(current)
        
        result = "".join(stack[0:len(num)-k]).lstrip("0")
        
        if len(result):
            return result
        else:
            return "0"