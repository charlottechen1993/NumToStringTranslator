import re

list_tenth_pt1 = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
list_tenth_s = ['', '-ten', '-twentie', '-thirtie', '-fortie', '-fiftie', '-sixtie', '-seventie', '-eightie', '-ninetie']
list_tenth_full = ['', 'tenth', 'twentieth', 'thirtieth', 'fortieth', 'fiftieth', 'sixtieth', 'seventieth', 'eightieth', 'ninetieth']
list_tens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_tenth = ['', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth']
list_ones_th = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
list_ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# returns the string expression of numbers from 10-99
def ConvertTens(input_tens):
	tenth_digit = ''
	ones_digit = ''

	tens = int(input_tens)
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

def ConvertOnes(input_ones):
	ones = int(input_ones)
	return list_ones[ones]







