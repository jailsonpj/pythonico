word = 'banana'

new_word = word.upper()
print(new_word)


print('a' in 'banana')

def in_both(word1,word2):
	for letter in word1:
		if letter in word2:
			print(letter)


def in_palindrome(word1,word2):
	if word1[::] in word2[::-1]:
		print("É palindrono")


in_both('jaca',word)
in_both('apples','oranges')

print(word[::-1])
in_palindrome('pots','stop')