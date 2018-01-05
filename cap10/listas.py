def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res


def only_upper(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
	return res

t = ['JAJA' , 'bruna' , 'LUCAS']

#saida = capitalize_all(t)
saida = only_upper(t)

for i in range(len(saida)):
	print(saida[i])