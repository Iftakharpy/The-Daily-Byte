from typing import List


# O(n+m+u) time
# O(u) space unique words
def uncommon_words(sentence_1: str, sentence_2:str) -> List[str]:
	cache = {}
	# O(n)
	for word in sentence_1.split(" "):
		if cache.get(word):
			cache[word] += 1
		else:
			cache[word] = 1
	# O(m)
	for word in sentence_2.split(" "):
		if cache.get(word):
			cache[word] += 1
		else:
			cache[word] = 1
	
	res = []
	# O(u) unique words
	for word,count in cache.items():
		if count==1:
			res.append(word)

	return res
