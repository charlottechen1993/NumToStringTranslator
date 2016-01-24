import sys
import re
from trans_date import * 
from trans_money import *

# user_input = raw_input("Please specify a file: ") 
output_string = ''

# with open(user_input, 'r') as f:
with open('more.txt','r') as f:
	text = f.read()

list_thousand = ['', 'one thousand', 'two thousand', 'three thousand', 'four thousand', 'five thousand', 'six-thousand', 'seven-thousand', 'eigth-thousand', 'nine-thousand']
list_hundred = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six-hundred', 'seven-hundred', 'eigth-hundred', 'nine-hundred']
list_full_tenth = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
list_full_tenth_s = ['s', '-tens', '-twenties', '-thirties', '-forties', '-fifties', '-sixties', '-seventies', '-eighties', '-nineties']
list_tenth = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
list_th = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

# split entire text into substring by ',', '.', and '\n'
master_list = (re.split(r'(\s+,\s+|\s+\n|\s+\.\s+)',text))

print master_list 
print '\n'

def concatSubstring(input_str, output_string):
	for print_char in input_str:
		output_string += print_char
	return output_string

def hasNumbers(input_str):
	return bool(re.search(r'\d', input_str))


# Traverse through the splitted list 
for substring in master_list:
	# Check if list contains numbers
	allStrings = hasNumbers(substring)

	# if substring doesn't contain number, print each char in substring
	if allStrings == False:
		output_string = concatSubstring(substring, output_string)

	# if substring contains number, find all occurences of number, translate, and print
	else:
		# =========================
		# ======== Percent ========
		# =========================
		substring = substring.replace('%', 'percent')

		# ======================
		# ======== Date ========
		# ======================
		new_substring_date = EvaluateDate(substring)
		substring = substring.replace(substring, new_substring_date)

		# =======================
		# ======== Money ========
		# =======================
		new_substring_money = EvaluateMoney(substring)
		substring = substring.replace(substring, new_substring_money)


		# decimal

		output_string = concatSubstring(substring, output_string)

# print output_string
