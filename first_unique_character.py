class Solution:
	def firstUniqChar(self, s: str) -> int:

		for x in s:
			if s.count(x) == 1:
				return s.find(x)

		return -1