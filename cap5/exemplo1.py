# divisão pelo piso e módulo

minutes = 105
resultado = minutes/60

print(resultado) #essa divisão devolve um ponto flutuante como resultado

resultado2 = minutes // 60

print(resultado2) #essa divisão pelo piso devolve um numero inteiro


#Recursividade

def countdown(n):
	if n <= 0:
		print('Blastoff!')
	else:
		print(n)
		countdown(n-1)

countdown(3)


