import re

list_tenth_pt1 = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
list_tenth_full = ['', 'tenth', 'twentieth', 'thirtieth']
list_tens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_tenth = ['', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
list_ones_th = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
list_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# returns the string expression of numbers from 10-99
def ConvertTens(tens):
	tenth_digit = ''
	ones_digit = ''

	# [10, 20, 30, 40, 50, 60, 70, 80, 90]
	if tens == 90: return list_tenth_pt1[9]
	elif tens == 80: return list_tenth_pt1[8]
	elif tens == 70: return list_tenth_pt1[7]
	elif tens == 60: return list_tenth_pt1[6]
	elif tens == 50: return list_tenth_pt1[5]
	elif tens == 40: return list_tenth_pt1[4]
	elif tens == 30: return list_tenth_pt1[3]
	elif tens == 20: return list_tenth_pt1[2]
	elif tens == 10: return list_tenth_pt1[1]
	else:
		# [21-99]
		if tens/90>0:
			tenth_digit = list_tenth_pt1[9]
		elif tens/80>0:
			tenth_digit = list_tenth_pt1[8]
		elif tens/70>0:
			tenth_digit = list_tenth_pt1[7]
		elif tens/60>0:
			tenth_digit = list_tenth_pt1[6]
		elif tens/50>0:
			tenth_digit = list_tenth_pt1[5]
		elif tens/40>0:
			tenth_digit = list_tenth_pt1[4]
		elif tens/30>0:
			tenth_digit = list_tenth_pt1[3]
		elif tens/20>0:
			tenth_digit = list_tenth_pt1[2]
		else:
			# [11-19]
			return list_tens[tens%10]
		onesdigit = list_ones[tens%10]
	return tenth_digit + ' ' + onesdigit

# returns the string expression of numbers from [0-9]
def ConvertOnes(ones):
	return list_ones[ones]


def ConvertYears(input_year):
	new_string = ''
	# 20XX or 200X
	eng_tens = '' 
	eng_ones = ''
	# XX56 or #19XX
	eng_pt1 = ''
	eng_pt2 = ''

	# Year > 2000
	if input_year[0] == '2':
		year = int(input_year)
		new_string += 'two thousand'
		tens = year%2000
		# 2010-2099
		if tens != 0 and tens >= 10:
			eng_tens = ConvertTens(tens) 
			new_string += ' '
			new_string += eng_tens
		# 2001-2009
		elif tens != 0 and tens < 10:
			eng_ones = ConvertOnes(tens)
			new_string += ' '
			new_string += eng_ones
	# Year < 2000
	elif input_year[0] == 1:
		year = int(input_year)
		year_pt1 = re.search(r'\d{2}', year)
		year_pt2 = re.search(r'\d[3:4]', year) 
		eng_pt1 = ConvertTens(year_pt1.group(1))
		eng_pt2 = ConvertTens(year_pt2.group(1))
		new_string += eng_pt1
		new_string += ' '
		new_string += eng_pt2

	return new_string


# Translate any date format numbers in substring
def EvaluateDate(substring):
	new_str = ''
	# Format 1: e.g. Oct. 26
	# re.findall(r'(?:jan|feb|mar|april|may|june|july|aug|sep|oct|nov|dec|january|february|march|august|september|october|november|december)\.*\s+\d{1,2}', 'Jan. 1 and Aug. 19 and then September 6', re.IGNORECASE)	# Format 2: e.g. October 26 or Oct 26
	# reg_date = re.findall(r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|March|April|May|June|Jun|July|Aug|Sept|Oct|Nov|Dec)\s(\d*).*', input_str, re.IGNORECASE)
	
	# if reg_date_dot:
	# 	date_str = transDate(reg_date_dot.group(2))
	# 	new_sentence = reg_date_dot.replace
	# 	return date_str
	# elif reg_date:
	# 	date_str2 = transDate(reg_date.group(2))

	# =================================================
	# Format 1: to, by, from, in, of, the, and, or 2015
	# =================================================
	new_substring = ''
	reg_year = re.findall(r'[to|by|from|in|of|the|and|or]+\s\d{4}', substring, re.IGNORECASE)
	if reg_year:
		for r in range(0, len(reg_year)):
			full_year = re.search(r'(\d+)', reg_year[int(r)])
			new_substring = ConvertYears(full_year.group(1))
			substring = substring.replace(full_year.group(1), new_substring)
	# if cur num is no associated with date, return original input_str
	return substring


def transDate(input_num):
	# [1-9]
	if(len(str(input_num))==1):
		return list_ones_th[input_num]
	elif(len(str(input_num))==2):
		tenth_digit = ''
		ones_digit = ''
		# [10, 20, 30]
		if input_num == 30: return list_tenth_full[3]
		elif input_num == 20: return list_tenth_full[2]
		elif input_num == 10: return list_tenth_full[1]
		else:
			if input_num/30>0:
				tenth_digit = list_tenth_pt1[3]
			elif input_num/20>0:
				tenth_digit = list_tenth_pt1[2]
			else:
				# [11-19]
				return list_tenth[input_num%10]
			onesdigit = list_ones_th[input_num%10]
		# [21-31]
		return tenth_digit + ' ' + onesdigit
	return 'ERROR!!!'



