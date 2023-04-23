ultimo = 1
penultimo = 1

for numero in range(1,11):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print("-", termo) 