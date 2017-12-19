
fruit = 'banana'
index = 0
while index < len(fruit):
	letter =  fruit[index]
	#print(letter) imprime cada letra em uma unica linha
	index = index + 1


#print(fruit[:3]) imprime as tres primeiras letras da palavra banana
#print(fruit[:])	imprime a palavra banana

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)