class Solution:
    def frequencySort(self, s: str) -> str:
        dictionary = {}
        result = ''
        
        for c in s:
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1
                
        sorted_dict = sorted(dictionary, key = lambda i : dictionary[i], reverse = True)

        for char in sorted_dict:
            result += char * dictionary[char]
            
        return result