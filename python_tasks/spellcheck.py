#!/usr/bin/python3
#cat /usr/share/dict/words > words.txt
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
