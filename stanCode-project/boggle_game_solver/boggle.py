"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global variable

# To realize whether we input the wrong format of the letter.
fail = 0
whole_str = []
words_lst = []


def main():
	"""
	TODO:
	"""
	global whole_str
	one = str(input('1 row of letters: '))
	certify(one)
	combined_rows = []
	if fail == 0:
		one = one.lower()
		combined_rows.append(one)
		two = str(input('2 row of letters: '))
		certify(two)
		if fail == 0:
			two = two.lower()
			combined_rows.append(two)
			three = str(input('3 row of letters: '))
			certify(three)
			if fail == 0:
				three = three.lower()
				combined_rows.append(three)
				four = str(input('4 row of letters: '))
				certify(four)
				if fail == 0:
					four = four.lower()
					combined_rows.append(four)
					# In order to change four rows into one line.
					combined_rows.append('')
					combined_rows = list(' '.join(combined_rows))
					# Every letter have a chance to be the first letter in the word.
					for i in range(0, 32, 2):
						# Add the letter as the first letter of the word.
						current_str = list(combined_rows[i])
						first = combined_rows[i]
						combined_rows[i] = 0
						find_word(combined_rows, i, current_str)
						combined_rows[i] = first
					print(f'There are {len(whole_str)} words in total.')



def certify(input_str):
	# To certify that the words we input is the exact format that we want to input.
	global fail
	if len(input_str) != 7:
		print('Illegal input')
		fail += 1
	else:
		for i in range(len(input_str)):
			if i % 2 == 1:
				if input_str[i] != ' ':
					print('Illegal input')
					fail += 1
					break
			else:
				if input_str[i].isalpha() == False:
					print('Illegal input')
					fail += 1
					break


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global words_lst
	with open(FILE, 'r') as f:

		for line in f:
			words = str(line.strip())
			words_str = ''
			for i in range(len(words)):
				if words[i].isalpha() == True:
					words_str += words[i]
			# Only store the words which length is bigger or equal to four.
			if len(words_str) >= 4:
				words_lst.append(words_str)
		# Return a list of the whole words in the dictionary.
		return words_lst


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(words_lst)):
		return str(words_lst[i]).startswith(str(sub_s))


def find_word(combined_rows, i, current_str):
	global words_lst
	words_lst = read_dictionary()
	find_word_helper(current_str, words_lst, combined_rows, i, whole_str)


def find_word_helper(current_str, file, rows_combined, i, all_str):
	# Search whether the combination of the first two words exists.
	if len(current_str) == 2:
		temp_str = list(current_str)
		if has_prefix(temp_str) == True:
			find_word_helper(current_str, file, rows_combined, i, all_str)

	# Base case
	if len(current_str) >= 4:
		current_str = ''.join(current_str)
		if str(current_str) in file:
			if str(current_str) not in all_str:
				whole_str.append(str(current_str))
				print(f'Found:  {current_str}')
				current_str = list(current_str)
				# the location in its row, location = 0, 2, 4, 6.
				x = (i % 8)
				# the row the letter locates in, row = 0, 1, 2, 3.
				y = (i // 8)
				# Find the letters in the same row.
				for j in range(-2, 4, 2):
					# Find the letters in the different rows.
					for k in range(-1, 2, 1):
						location_x = x + j
						location_y = y + k
						# Set the range of selection:
						if (0 <= location_x <= 6) & (0 <= location_y <= 3):
							# Choose
							if str(rows_combined[location_x + (8 * location_y)]).isalpha() == True:
								current_str.append(rows_combined[location_x + (8 * location_y)])
								disappear = rows_combined[location_x + (8 * location_y)]
								rows_combined[location_x + (8 * location_y)] = 0
								# Explore
								last_i = i
								i = location_x + (8 * location_y)
								find_word_helper(current_str, file, rows_combined, i, whole_str)
								# Un-Choose
								current_str.pop()
								rows_combined[location_x + (8 * location_y)] = disappear
								i = last_i

	# Recursion
	else:
		# the location in its row, location = 0, 2, 4, 6.
		x = (i % 8)
		# the row the letter locates in, row = 0, 1, 2, 3.
		y = (i // 8)
		# Find the letters in the same row.
		for j in range(-2, 4, 2):
			# Find the letters in the different rows.
			for k in range(-1, 2, 1):
				location_x = x + j
				location_y = y + k
				# Set the range of selection:
				if (0 <= location_x <= 6) & (0 <= location_y <= 3):
					# Choose
					if str(rows_combined[location_x + (8 * location_y)]).isalpha() == True:
						current_str.append(rows_combined[location_x + (8 * location_y)])
						disappear = rows_combined[location_x + (8 * location_y)]
						rows_combined[location_x + (8 * location_y)] = 0
					# Explore
						last_i = i
						i = location_x + (8 * location_y)
						find_word_helper(current_str, file, rows_combined, i, whole_str)
					# Un-Choose
						current_str.pop()
						rows_combined[location_x + (8 * location_y)] = disappear
						i = last_i


if __name__ == '__main__':
	main()
