import re
list_tens_2 = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
list_tens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# returns the string expression of numbers from 0-9
def ConvertOnes(input_ones):
	ones = int(input_ones)
	return list_ones[ones]

# returns the string expression of numbers from 10-99
def ConvertTens(input_tens):
	tenth_digit = ''
	ones_digit = ''

	tens = int(input_tens)
	# [10, 20, 30, 40, 50, 60, 70, 80, 90]
	if tens == 90: return list_tens_2[9]
	elif tens == 80: return list_tens_2[8]
	elif tens == 70: return list_tens_2[7]
	elif tens == 60: return list_tens_2[6]
	elif tens == 50: return list_tens_2[5]
	elif tens == 40: return list_tens_2[4]
	elif tens == 30: return list_tens_2[3]
	elif tens == 20: return list_tens_2[2]
	elif tens == 10: return list_tens_2[1]
	else:
		# [21-99]
		if tens/90>0:
			tenth_digit = list_tens_2[9]
		elif tens/80>0:
			tenth_digit = list_tens_2[8]
		elif tens/70>0:
			tenth_digit = list_tens_2[7]
		elif tens/60>0:
			tenth_digit = list_tens_2[6]
		elif tens/50>0:
			tenth_digit = list_tens_2[5]
		elif tens/40>0:
			tenth_digit = list_tens_2[4]
		elif tens/30>0:
			tenth_digit = list_tens_2[3]
		elif tens/20>0:
			tenth_digit = list_tens_2[2]
		else:
			# [11-19]
			return list_tens[tens%10]
		onesdigit = list_ones[tens%10]
	return tenth_digit + ' ' + onesdigit

# returns the string expression of numbers from 100-999
def ConvertHundreds(input_huns):
	hundred_digit = ''

	single_hundred_digit = str(input_huns)[0]
	if int(input_huns[0]) != 0:
		hundred_digit += list_ones[int(single_hundred_digit)]
		hundred_digit += ' hundred '

	single_tens_digit = str(input_huns)[1] + str(input_huns)[2]
	int_single_tens_digit = int(single_tens_digit)

	# if NOT 100
	if int_single_tens_digit != 0:
		# e.g. 101
		if len(str(int_single_tens_digit))==1:
			hundred_digit += 'and '
			hundred_digit += ConvertOnes(single_tens_digit)
		elif len(str(int_single_tens_digit))==2:
			tens_digit = ConvertTens(single_tens_digit)
			# hundred_digit += ' '
			hundred_digit += tens_digit

	return hundred_digit

# returns the string expression of numbers from 1,000-9,999
def ConvertThousands(input_thou):
	thousand_digit = ''

	single_thou_digit = str(input_thou)[0]
	thousand_digit += list_ones[int(single_thou_digit)]
	thousand_digit += ' thousand'

	single_hun_digit =  str(input_thou)[1] + str(input_thou)[2] + str(input_thou)[3]
	int_single_hun_digit = int(single_hun_digit)

	# e.g if NOT 1,000
	if int_single_hun_digit != 0:
		# e.g. 1,001
		if str(input_thou)[1] == '0' and str(input_thou)[2] == '0':
			thousand_digit += ' '
			thousand_digit += ConvertOnes(single_hun_digit)
		# e.g 1,010
		elif str(input_thou)[1] == '0':
			thousand_digit += ' '
			thousand_digit += ConvertTens(single_hun_digit)
		# e.g. 1,100
		else: 
			hundreds_digit = ConvertHundreds(single_hun_digit)
			thousand_digit += ' '
			thousand_digit += hundreds_digit

	return thousand_digit

# returns the string expression of numbers from 10,000-99,999
def ConvertTenThousands(input_ten_thou):
	tenthousand_digit = ''

	single_tenthou_digit = str(input_ten_thou)[0] + str(input_ten_thou)[1]
	tenthousand_digit += ConvertTens(single_tenthou_digit)
	tenthousand_digit += ' thousand'

	single_thou_digit = str(input_ten_thou)[2] + str(input_ten_thou)[3] + str(input_ten_thou)[4]
	int_single_thou_digit = int(single_thou_digit)

	if int_single_thou_digit != 0:
		# e.g. 10,001
		if len(str(int_single_thou_digit)) == 1:
			tenthousand_digit += ' and '
			tenthousand_digit += ConvertOnes(single_thou_digit)
		# e.g. 10,010
		elif len(str(int_single_thou_digit)) == 2:
			tenthousand_digit += ' '
			tenthousand_digit += ConvertTens(single_thou_digit)
		# e.g. 10,100
		else:
			thousands_digit = ConvertHundreds(single_thou_digit)
			if single_thou_digit !=0:
				tenthousand_digit += ' '
				tenthousand_digit += thousands_digit
	return tenthousand_digit

# returns the string expression of numbers from 100,000-999,999
def ConvertHundredThousands(input_hun_thou):
	hunthousand_digit = ''

	single_hunthou_digit = str(input_hun_thou)[0] + str(input_hun_thou)[1] + str(input_hun_thou)[2]
	hunthousand_digit += ConvertHundreds(single_hunthou_digit)
	hunthousand_digit += ' thousand'

	single_thou_digit = str(input_hun_thou)[3] + str(input_hun_thou)[4] + str(input_hun_thou)[5]
	int_single_thou_digit = int(single_thou_digit)
	if int_single_thou_digit != 0:
		# e.g. 100,001
		if len(str(int_single_thou_digit)) == 1:
			hunthousand_digit += ' and '
			hunthousand_digit += ConvertOnes(single_thou_digit)
		# e.g. 100,010
		elif len(str(int_single_thou_digit)) == 2:
			hunthousand_digit += ' '
			hunthousand_digit += ConvertTens(single_thou_digit)
		# e.g 100,100
		else:
			thousands_digit = ConvertHundreds(single_thou_digit)
			if single_thou_digit !=0:
				hunthousand_digit += ' '
				hunthousand_digit += thousands_digit
	return hunthousand_digit

# [1,000,000-9,999,999]
def ConvertMillion(input_million):
	million_digit = ''
	hunthousand_digit = ''

	single_million_digit = str(input_million)[0]
	million_digit += list_ones[int(single_million_digit)]
	million_digit += ' million'

	single_hunthou_digit =  str(input_million)[1] + str(input_million)[2] + str(input_million)[3] + str(input_million)[4] + str(input_million)[5] + str(input_million)[6]
	int_single_hunthou_digit = int(single_hunthou_digit)

	# e.g if NOT 1,000,000
	if int_single_hunthou_digit != 0:
		million_digit += ' '
		million_digit += ConvertHundredThousands(single_hunthou_digit)

	return million_digit

# [10,000,000-99,999,999]
def ConvertTenMillion(input_tenmillion):
	tenmillion_digit = ''

	single_tenmillion_digit = str(input_tenmillion)[0] + str(input_tenmillion)[1]
	tenmillion_digit += ConvertTens(single_tenmillion_digit)
	tenmillion_digit += ' million'

	single_hunthou_digit =  str(input_tenmillion)[2] + str(input_tenmillion)[3] + str(input_tenmillion)[4] + str(input_tenmillion)[5] + str(input_tenmillion)[6] + str(input_tenmillion)[7]
	int_single_hunthou_digit = int(single_hunthou_digit)

	# e.g if NOT 10,000,000
	if int_single_hunthou_digit != 0:
		tenmillion_digit += ' '
		tenmillion_digit += ConvertHundredThousands(single_hunthou_digit)

	return tenmillion_digit

# # [100,000,000-999,999,999]
def ConvertHunMillion(input_hunmillion):
	hunmillion_digit = ''

	single_hunmillion_digit = str(input_hunmillion)[0] + str(input_hunmillion)[1] + str(input_hunmillion)[2]
	hunmillion_digit += ConvertHundreds(single_hunmillion_digit)
	hunmillion_digit += ' million'

	single_hunthou_digit =  str(input_hunmillion)[3] + str(input_hunmillion)[4] + str(input_hunmillion)[5] + str(input_hunmillion)[6] + str(input_hunmillion)[7] + str(input_hunmillion)[8]
	int_single_hunthou_digit = int(single_hunthou_digit)

	# e.g if NOT 10,000,000
	if int_single_hunthou_digit != 0:
		hunmillion_digit += ' '
		hunmillion_digit += ConvertHundredThousands(single_hunthou_digit)

	return hunmillion_digit

def ConvertFullNumber(input_int):
	eng_full = ''

	# [0-9]
	if len(str(input_int))==1:
		eng_full = ConvertOnes(input_int)
	# [10-99]
	elif len(str(input_int))==2:
		eng_full = ConvertTens(input_int)
	# [100-999]
	elif len(str(input_int))==3:
		eng_full = ConvertHundreds(input_int)
	# [1,000-9,999]
	elif len(str(input_int))==4:
		eng_full = ConvertThousands(input_int)
	# [10,000-99,999]
	elif len(str(input_int))==5:
		eng_full = ConvertTenThousands(input_int)
	# [100,000-999,999]
	elif len(str(input_int))==6:
		eng_full = ConvertHundredThousands(input_int)
	# [1,000,000-9,999,999]
	elif len(str(input_int))==7:
		eng_full = ConvertMillion(input_int)
	# [10,000,000-99,999,999]
	elif len(str(input_int))==8:
		eng_full = ConvertTenMillion(input_int)
	# # [100,000,000-999,999,999]
	elif len(str(input_int))==9:
		eng_full = ConvertHunMillion(input_int)

	return eng_full


def ConvertDecimal(input_dec):
	eng_decimal = ''
	integer = ''
	decimal = ''
	# split number into integer and decimal parts
	split_dec = str(input_dec).split('.')
	integer = split_dec[0]
	decimal = split_dec[1]
	eng_decimal += ConvertFullNumber(integer)
	eng_decimal += ' point'
	for i in range(0, len(decimal)):
		eng_decimal += ' '
		eng_decimal += ConvertOnes(decimal[i])

	return eng_decimal

def EvaluateOthersFull(substring):
	reg_int = re.findall(r'(\d+(?:(?:\,\d{3})+)?)', substring)

	if reg_int:
		for r6 in range(0, len(reg_int)):
			new_substring = ''
			ori_int = reg_int[r6]
			integer = reg_int[r6].replace(',', '')

			new_substring += ConvertFullNumber(integer)

			# print ori_int + " : " + new_substring

			substring = substring.replace(ori_int, new_substring)

	return substring

def EvaluateOthersDecimal(substring):
	# .4 and 1,000.2332 and 1000 and 2.34
	reg_dec = re.findall(r'(\d+(?:(?:\,\d{3})+)?(?:\.\d+))', substring)
	if reg_dec:
		for r5 in range(0, len(reg_dec)):
			new_substring = ''
			ori_dec = reg_dec[r5]
			decimal = reg_dec[r5].replace(',', '')

			new_substring += ConvertDecimal(decimal)

			# print ori_dec + " : " + new_substring

			substring = substring.replace(ori_dec, new_substring)

	return substring





