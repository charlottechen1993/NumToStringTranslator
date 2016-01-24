import sys
import re
from trans_date import * 
from trans_money import *
from trans_fraction import *

# user_input = raw_input("Please specify a file: ") 
output_string = ''

# with open(user_input, 'r') as f:
with open('my_test.txt','r') as f:
	text = f.read()

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

		# =======================
		# ====== Fraction =======
		# =======================
		new_substring_fraction = EvaluateFraction(substring)
		substring = substring.replace(substring, new_substring_fraction)

		# =======================
		# ======= Others ========
		# =======================
		# new_substring_others2 = EvaluateOthersDecimal(substring)
		# substring = substring.replace(substring, new_substring_others2)

		# new_substring_others = EvaluateOthersFull(substring)
		# substring = substring.replace(substring, new_substring_others)
		

		output_string = concatSubstring(substring, output_string)

# print output_string
