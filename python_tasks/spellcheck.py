
def spellcheck():
	sentence= input("Write your sentence?")
	data = open("words.txt").readlines()
	words = list(map(lambda x: x.strip(), data))
	result = sentence.split()
	for item in result:
		if item in words:
			continue
		else:
			return item
print(spellcheck())
