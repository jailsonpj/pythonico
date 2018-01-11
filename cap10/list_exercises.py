import sys

def nested_sum(t): #retorna a soma dos elementos da lista
    acum = 0
    for nested in t:
        acum += sum(nested)
    return acum

def cumsum(t): #retorn uma lista com a soma dos dos elemento antriores
    aux = []
    acum = 0
    for i in t:
        acum += i
        aux.append(acum)
    return aux

def middle(t): #retorna uma lista menos o primeiro e o ultimo elemento
    return t[1:-1]

def chop(t): #deleta o primeiro e o ultimo elemento da lista
    del t[0]
    del t[-1]

def is_sorted(t): #verifica se a lista está ordenada
    return t == sorted(t)

def is_anagram(word1,word2):
    return sorted(word1) == sorted(word2)

def has_duplicates(s):
    t = list(s)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

lista = list(input())

t = [[1,2],[3],[4,5,6]]
t1 = [1,2,3]
t3 = [1,2,3,4]
print(lista)
print(nested_sum(t))
print(cumsum(t1))
print(middle(t3))
print(chop(t3))
print(is_sorted(t1))
print(is_anagram('amor','roma'))
#print(nested_sum(t4))
