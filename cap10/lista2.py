
w = 'spam'
u = list(w)
print(u)


s = 'pining for the fjords'
t = s.split()

print(t)


#uso de delimitador
ls = 'spam-spam-spam'
delimiter = '-'
aux = ls.split(delimiter)
print(aux)

deli = ' '
aux1 = deli.join(t)
print(aux1)