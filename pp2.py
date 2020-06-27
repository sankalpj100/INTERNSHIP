

def PalindromePermutation(phrase):
	oddCount = 0
	b = phrase.replace(" ","")

	phraselist = list(b)
	getList = uniquechars(phraselist)
	countTable = charCounter(getList, phraselist)
	print(phraselist)
	print(booleanPP(oddCount,countTable))


def uniquechars(phraselist):
	uniquelist = []
	for ele in phraselist:
		if ele not in uniquelist:
			uniquelist.append(ele)
	return uniquelist

def charCounter(uniquelist, phraselist):
	hashtableC = {}
	for ele in uniquelist:
		countofchar = 0
		for ele2 in phraselist:
			if (ele == ele2):
				countofchar += 1
		hashtableC[ele] = countofchar
	return hashtableC

def booleanPP(oddCount,hashtableC):
	x = 0
	for ele in hashtableC:
		if x % 2 == 1:
			oddCount += 1
		elif oddCount < 1:
			x += hashtableC[ele]
		if oddCount > 1:
			return False
	if oddCount < 1:
		return True
		


phrase = (input("Enter the phrase :"))
PalindromePermutation(phrase)

