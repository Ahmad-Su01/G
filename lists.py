""" numere = [1, 2, 3, 10, 12, 14]

del numere[3]
# print(numere)

del numere
# print(numere)

numere = [1, 2, 3, 10, 12, 12, 14]

# Folosind pop

numere.pop()
print(numere)

# Folosind remove
numere.remove(12)
print(numere) """

""" text_mama = "Azi gateste"
lista_text = []
lista_text = text_mama.split(" ")
print(lista_text)
lista_text.insert(1, "mama")
print(lista_text)
text_mama_joined = " ".join(lista_text)
print(text_mama_joined) """

""" 
numere = [1, 3, 10, 7, 4, 14] # 6 numere

# Folosing nested list/ bucla pe bucla
for positia_primar in range(len(numere)):
    for positia_secundar in range(len(numere)):
        if numere[positia_primar] < numere[positia_secundar]:
            numere[positia_primar], numere[positia_secundar] = numere[positia_secundar], numere[positia_primar]

print(numere) 
"""

"""
    numere Romane: I, V, X, L, C, M, D, ...
    bucla si sami aduni valorile. Suma totala. Exemplu
    text = "MDCX"
    I = 1
    X = 9
    L = 50
    C = 100
    D = 500
    M = 1000
    
    Suma Numere Romane =  1000 + 500 + 100 + 10 = 1610
    
    Inainte de numere:
    V: I
    X: I
    L: X
    C: X
    M: C
    D: C
    Cate litere:
    1. Inspate 1 de litera.
    2. Infata 3 de litera.
    
    Exemplu:
    1. IX -> 9, XL -> 40
    2. XIII -> 13, LXXX -> 80
"""