import re
from base import * 

def EvaluateMoney(substring):
	# $ 1,000 billion; $ 3.5; $ 1,660
	reg_money = re.findall(r'([$])\s(\d+(?:(?:\,\d{3})+)?(?:\.\d+)?)\s?(?:(million|billion|trillion)?)', substring, re.IGNORECASE)

	if reg_money:
		for r3 in range(0, len(reg_money)):
			money = ''
			new_substring = ''
			ori_money = ''
			new_money_only = ''

			# store original full money expression for replacement
			ori_money += reg_money[r3][0]
			ori_money += ' '
			ori_money += reg_money[r3][1]
			if len(reg_money[r3][2])!=0:
				ori_money += ' '
				ori_money += reg_money[r3][2]

			full_money = reg_money[r3][1]
			money = full_money.replace(',', '')

			# decimal (e.g. $ 12.1)
			if '.' in str(money):
				# convert only decimal money
				new_money_only = ConvertDecimal(money)
				
			# full dollar amount (e.g. $ 6)
			else:
				new_money_only += ConvertFullNumber(money)

			# construct final new substring
			new_substring += new_money_only

			if len(reg_money[r3][2])!=0:
				new_substring += ' '
				new_substring += reg_money[r3][2]
			if reg_money[r3][1] == '1' and len(reg_money[r3][2])==0:
				new_substring += ' dollar'
			else:
				new_substring += ' dollars'

			# print ori_money + ' : ' + new_substring
			
			if len(new_substring) != 0:
				substring = substring.replace(ori_money, new_substring)

	return substring





