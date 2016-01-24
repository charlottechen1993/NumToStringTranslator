import re
from base import * 

list_tenth_pt1 = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
list_tenth_s = ['', '-ten', '-twentie', '-thirtie', '-fortie', '-fiftie', '-sixtie', '-seventie', '-eightie', '-ninetie']
list_tenth_full = ['', 'tenth', 'twentieth', 'thirtieth', 'fortieth', 'fiftieth', 'sixtieth', 'seventieth', 'eightieth', 'ninetieth']
list_tens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_tenth = ['', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
list_ones_th = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
list_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# returns the string expression of numbers from 10-99 (with 'th')
def ConvertTenth(input_tens):
	tenth_digit = ''
	ones_digit = ''

	tens = int(input_tens)
	# [10, 20, 30, 40, 50, 60, 70, 80, 90]
	if tens == 90: return list_tenth_full[9]
	elif tens == 80: return list_tenth_full[8]
	elif tens == 70: return list_tenth_full[7]
	elif tens == 60: return list_tenth_full[6]
	elif tens == 50: return list_tenth_full[5]
	elif tens == 40: return list_tenth_full[4]
	elif tens == 30: return list_tenth_full[3]
	elif tens == 20: return list_tenth_full[2]
	elif tens == 10: return list_tenth_full[1]
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
			return list_tenth[tens%10]
		onesdigit = list_ones_th[tens%10]
	return tenth_digit + ' ' + onesdigit

def ConvertTens_S(input_tens):
	tenth_digit = ''
	ones_digit = ''

	tens = int(input_tens)
	# [10, 20, 30, 40, 50, 60, 70, 80, 90]
	if tens == 90: return list_tenth_s[9]
	elif tens == 80: return list_tenth_s[8]
	elif tens == 70: return list_tenth_s[7]
	elif tens == 60: return list_tenth_s[6]
	elif tens == 50: return list_tenth_s[5]
	elif tens == 40: return list_tenth_s[4]
	elif tens == 30: return list_tenth_s[3]
	elif tens == 20: return list_tenth_s[2]
	elif tens == 10: return list_tenth_s[1]
	
	# if 1900s
	return 'hundreds'


# returns the string expression of numbers from [0-9] (with "th")
def ConvertOnes_th(input_ones):
	ones = int(input_ones)
	return list_ones_th[ones]

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
		new_string += ConvertThousands(input_year)
	# Year < 2000
	elif input_year[0] == '1':
		year = input_year
		year_pt1 = year[0:2]
		year_pt2 = year[2:4]
		eng_pt1 = ConvertTens(year_pt1)
		eng_pt2 = ConvertTens(year_pt2)
		new_string += eng_pt1
		new_string += ' '
		new_string += eng_pt2

	return new_string

def ConvertYearsWithS(input_year):
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
		# 2010s-2090s
		if tens == 0:
			return 'two thousands'
		elif tens != 0:
			eng_tens = ConvertTens_S(tens) 
			new_string += eng_tens
			new_string += 's'
	# Year < 2000
	elif input_year[0] == '1':
		year = input_year
		year_pt1 = year[0:2]
		year_pt2 = year[2:4]
		eng_pt1 = ConvertTens(year_pt1)
		eng_pt2 = ConvertTens_S(year_pt2)
		new_string += eng_pt1
		new_string += eng_pt2
		new_string += 's'

	return new_string

# Translate any date format numbers in substring
def EvaluateDate(substring):
	new_substring = ''

	# =========================
	# Format 1: Year on its own
	# =========================
	reg_year = re.findall(r'(?<=\s)\d{4}(?!s)(?!.)', substring)
	if reg_year:
		for r1 in range(0, len(reg_year)):
			full_year = re.search(r'(\d+)', reg_year[int(r1)])
			new_substring = ConvertYears(full_year.group(1))

			# print full_year.group(1) + ' : ' + new_substring
			substring = substring.replace(full_year.group(1), new_substring)

	# =========================
	# Format 1.5: Year with 's'
	# =========================
	reg_year_s = re.findall(r'(?<=\s)\d{4}(?=s)', substring)
	if reg_year_s:
		for r1_5 in range(0, len(reg_year_s)):
			full_year_s = re.search(r'(\d+)', reg_year_s[int(r1_5)])
			new_substring = ConvertYearsWithS(full_year_s.group(1))

			# print full_year_s.group(1) + ' : ' + new_substring
			substring = substring.replace(full_year_s.group(1), new_substring)

	# ===============================
	# Format 2: Oct. 26 or October 26
	# ===============================
	short_date = re.findall(r'(?:Jan|Feb|Mar|April|May|June|Jun|July|Jul|Aug|Sept|Sep|Oct|Nov|Dec|Janpercentuary|February|March|August|September|October|November|December)\.*\s+\d{1,2}', substring, re.IGNORECASE)
	if short_date:
		for r2 in range(0, len(short_date)):
			date = re.search(r'(\d+)', short_date[int(r2)])
			if len(str(date.group(1)))==1:
				new_substring = ConvertOnes_th(date.group(1))
			elif len(str(date.group(1)))==2:
				new_substring = ConvertTenth(date.group(1))

			# print date.group(1) + ' : ' + new_substring
			substring = substring.replace(date.group(1), new_substring)

	return substring


