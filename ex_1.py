# Numele si ssa facem slicing
# Sintax: variabila[initial : end : pas]

nume_primar : str = "Georgia"

print(nume_primar[0])
print(nume_primar[1])
print(nume_primar[3:])
print(nume_primar[:3])
print(nume_primar[::2])
print(nume_primar[-1])
print(nume_primar[-2])
print(nume_primar[: -2])
print(nume_primar[-2: ])

# Georgia
nume_copie = nume_primar
nume_copie = nume_copie[2 : 5]

print(nume_copie)
print(nume_primar)

# [:] -> Copie
nume_copie_2 = nume_primar[:]
nume_copie_2 = nume_copie_2[2:5]

print(nume_copie)
print(nume_primar)

# Inversul
print(nume_primar[::-1])