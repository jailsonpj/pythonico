def fatorial(n):
	if n == 0:
		return 1
	else:
		valor = fatorial(n-1)
		resultado = n * valor
		return resultado


def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

print(fatorial(5))
print(fibo(3))