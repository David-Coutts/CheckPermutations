'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

'''

def getInput():
	value = raw_input('Enter a value: ')
	return value

def compareStrings(stringOne, stringTwo):
	if len(stringOne) != len(stringTwo):
		return False
	else:
		if sorted(stringOne) == sorted(stringTwo):
			return True
		return False

def printResult(result):
	if result:
		print('The two strings are permutations of one another.')
	else:
		print('The two strings are not permutations of one another.')

def main():
	print("Enter two strings to determine if they're permutations of one another.")
	stringOne = getInput()
	stringTwo = getInput()
	result = compareStrings(stringOne, stringTwo)
	printResult(result)

if __name__ == '__main__':
	main()