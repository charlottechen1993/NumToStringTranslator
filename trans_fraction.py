import re
from base import * 

list_denom_pl = ['', '', 'halve', 'third', 'quarter', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

def ConvertFraction(numerator, denominator):
	new_substring = ''

	# X/2 - 1/10
	if int(denominator) <= 10 and int(denominator) != 1:
		# e.g. 1/2 1/3 1/4
		if int(numerator) == 1 :
			if int(denominator) == 2:
				new_substring += 'a half'
			elif int(denominator) == 4:
				new_substring += 'a quarter'
			else:
				new_substring += 'one '
				new_substring += list_denom_pl[int(denominator)]

		# e.g. 3/2 three halves; 5/6 five sixths
		else: 
			new_substring += ConvertFullNumber(numerator)

			if int(denominator) == 2:
				new_substring += ' halves'
			elif int(denominator) == 4:
				new_substring += ' quarters'
			else: 
				new_substring += ' '
				new_substring += list_denom_pl[int(denominator)]
				new_substring += 's'

	# X/1 or X/100
	else:
		new_substring += ConvertFullNumber(numerator)
		new_substring += ' over '
		new_substring += ConvertFullNumber(denominator)

	return new_substring


def EvaluateFraction(substring):

	reg_frac = re.findall('(\d+)?\s?(\d+)\\\\/(\d+)', substring)

	if reg_frac:
		for r4 in range(0, len(reg_frac)):
			new_substring = ''
			ori_frac = ''

			full_frac = reg_frac[int(r4)]
			# print full_frac

			full_num = full_frac[0]
			numerator = full_frac[1]
			denominator = full_frac[2]

			# Save original function expression for replacement
			if len(full_frac[0])!=0:
				ori_frac += full_frac[0]
				ori_frac += ' '
			ori_frac += full_frac[1]
			ori_frac += '\\/'
			ori_frac += full_frac[2]

			# print ori_frac

			# if fraction has full number portion
			if len(str(full_num))!=0:
				# Convert full number part
				if '.' not in str(full_num):
					new_substring += ConvertFullNumber(full_num)
					new_substring += ' and '
				else:
					new_substring += ConvertDecimal(full_num)
					new_substring += ' and '

			# Convert denominator and numerator
			new_substring += ConvertFraction(numerator, denominator)

			# print ori_frac + " : " + new_substring

			# replace original fraction
			substring = substring.replace(ori_frac, new_substring)

	return substring





