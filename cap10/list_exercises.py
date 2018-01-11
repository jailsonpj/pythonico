
def nested_sum(t):
    acum = 0
    for nested in t:
        acum += sum(nested)
    return acum

t = [[1,2],[3],[4,5,6]]
print(nested_sum(t))
