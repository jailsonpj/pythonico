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

def ack(m,n):
	if m == 0:
		return n+1
	elif m > 0 and n == 0:
		return ack(m-1,1)
	else:
		return ack(m-1,ack(m,n-1))


print(fatorial(5))
print(fibo(3))
print(ack(3,4))