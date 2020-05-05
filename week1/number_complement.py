class Solution:
	def findComplement(self, num: int) -> int:

		binary = bin(num)[2:]
		result = list(range(len(binary)))
		i = 0

		while i < len(binary):
			if binary[i] == '1':
				result[i] = '0'
			else:
				result[i] = '1'
			i += 1
		
		return int(''.join(result),2)