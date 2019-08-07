'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

'''

def compareStrings(stringOne, stringTwo):
	dictOne = {}
	dictTwo = {}

	if len(stringOne) != len(stringTwo):
		printResult(False)

	for i in stringOne:
		if i in dictOne:
			dictOne[i] += 1
		else:
			dictOne[i] = 1

	for i in stringTwo:
		if i in dictTwo:
			dictTwo[i] += 1
		else:
			dictTwo[i] = 1

	printResult(dictOne == dictTwo)


def printResult(result):
	if result:
		print('The two strings are permutations of one another.')
	else:
		print('The two strings are not permutations of one another.')

def main():
	print("Enter two strings to determine if they're permutations of one another.")
	print("Enter first string:")
	stringOne = input()
	print("Enter second string:")
	stringTwo = input()
	compareStrings(stringOne, stringTwo)

if __name__ == '__main__':
	main()