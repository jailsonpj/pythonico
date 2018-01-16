aux = { }

for linha in open('words.txt'):
    (nome,valor) = linha.split(' ')
    if nome not in aux:
        aux[nome] = valor

print(aux)
