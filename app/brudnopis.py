lista = [['Outskirts Shop', 27.36], ["Shop '24/7'", 29.24], ['Central Shop', 36.39]]

values = []
for value in lista:
    values.append(value[1])


var = all(value > 15 for value in values)
print(var)