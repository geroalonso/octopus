from num2words import num2words

def num_to_cur (number):
	string = num2words(number, to='currency')
	song = 'cold, cold heart'
	# replacing 'euros' with 'dollars'
	string = string.title().replace('Euro,', 'Dollars, with')
	return string

