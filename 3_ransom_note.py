class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        if ransomNote == "":
            return True
        for x in ransomNote:
            if x!= '\0' and ransomNote.count(x) <= magazine.count(x):
                result = True
            else:
                return False
                
        return result