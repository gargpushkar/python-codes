# Integer to Roman Numeral
# Given an integer num, convert it to a roman numeral.

# Roman numerals are denoted by a combination of some symbols.

# Value	Symbol
# 1	       I
# 5	       V
# 10	   X
# 50	   L
# 100	   C
# 500	   D
# 1000	   M

class Solution:
	def integerToRoman(self, num: int) -> str:
		# add your logic here
		roman_list = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5,], ["IV", 4,], ["I", 1]]
		ans = ""
		for i in roman_list:
			key = i[0]
			value = i[1]
			while num >= value:
				ans += key
				num -= value
		return ans


