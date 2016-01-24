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
	if len(str(input_huns)) == 3:
		hundred_digit += list_ones[int(single_hundred_digit)]
		hundred_digit += ' hundred'

	single_tens_digit = str(input_huns)[1] + str(input_huns)[2]
	int_single_tens_digit = int(single_tens_digit)

	# if NOT 100
	if int_single_tens_digit != 0:
		# e.g. 101
		if len(str(int_single_tens_digit))==1:
			hundred_digit += ' and '
			hundred_digit += ConvertOnes(int_single_tens_digit)
		elif len(str(int_single_tens_digit))==2:
			tens_digit = ConvertTens(single_tens_digit)
			hundred_digit += ' '
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
			thousand_digit += ConvertOnes(int_single_hun_digit)
		# e.g 1,010
		elif str(input_thou)[1] == '0':
			thousand_digit += ' '
			thousand_digit += ConvertTens(int_single_hun_digit)
		# e.g. 1,100
		else: 
			hundreds_digit = ConvertHundreds(int_single_hun_digit)
			thousand_digit += ' '
			thousand_digit += hundreds_digit

	return thousand_digit

# returns the string expression of numbers from 10,000-99,999
def ConvertTenThousands(input_ten_thou):
	tenthousand_digit = ''

	single_tenthou_digit = str(input_ten_thou)[0] + str(input_ten_thou)[1]
	tenthousand_digit += ConvertTens(int(single_tenthou_digit))

	single_thou_digit = str(input_ten_thou)[2] + str(input_ten_thou)[3] + str(input_ten_thou)[4]
	int_single_thou_digit = int(single_thou_digit)
	
	if int_single_thou_digit != 0:
		# e.g. 10,001
		if len(str(int_single_thou_digit)) == 1:
			tenthousand_digit += ' and '
			tenthousand_digit += ConvertOnes(int_single_thou_digit)
		# e.g. 10,010
		elif len(str(int_single_thou_digit)) == 2:
			tenthousand_digit += ' '
			tenthousand_digit += ConvertTens(int_single_thou_digit)
		# e.g. 10,100
		else:
			thousands_digit = ConvertHundreds(str(single_thou_digit))
			if single_thou_digit !=0:
				tenthousand_digit += ' thousand'
				tenthousand_digit += ' '
				tenthousand_digit += thousands_digit
	else:
		tenthousand_digit += ' thousand'
	return tenthousand_digit

# returns the string expression of numbers from 100,000-999,999
def ConvertHundredThousands(input_hun_thou):
	hunthousand_digit = ''

	single_hunthou_digit = str(input_hun_thou)[0] + str(input_hun_thou)[1] + str(input_hun_thou)[2]
	hunthousand_digit += ConvertHundreds(int(single_hunthou_digit))

	single_thou_digit = str(input_hun_thou)[3] + str(input_hun_thou)[4] + str(input_hun_thou)[5]
	int_single_thou_digit = int(single_thou_digit)
	if int_single_thou_digit != 0:
		# e.g. 100,001
		if len(str(int_single_thou_digit)) == 1:
			hunthousand_digit += ' and '
			hunthousand_digit += ConvertOnes(int_single_thou_digit)
		# e.g. 100,010
		elif len(str(int_single_thou_digit)) == 2:
			hunthousand_digit += ' '
			hunthousand_digit += ConvertTens(int_single_thou_digit)
		# e.g 100,100
		else:
			thousands_digit = ConvertHundreds(str(single_thou_digit))
			if single_thou_digit !=0:
				hunthousand_digit += ' thousand'
				hunthousand_digit += ' '
				hunthousand_digit += thousands_digit
	else:
		hunthousand_digit += ' thousand'
	return hunthousand_digit

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

	return eng_full


def ConvertDecimal(input_dec):
	eng_decimal = ''

	integer = ''
	decimal = ''
	# split number into interger and decimal parts
	split_dec = str(input_dec).split('.')
	integer = split_dec[0]
	decimal = split_dec[1]
	eng_decimal += ConvertFullNumber(integer)
	eng_decimal += ' point'
	for i in range(0, len(decimal)):
		eng_decimal += ' '
		eng_decimal += ConvertOnes(decimal[i])

	return eng_decimal

