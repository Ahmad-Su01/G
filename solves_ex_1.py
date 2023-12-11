"""
1.Expresia de matematica  este X - X ^ 2 + X ^ 4. X poate fi ori ce numar. Printeaza resultatul.

2.Ai 5 variabile de int, gasestemi media (averagul).
Variabile sunt:
num_1 : int = 20
num_2 : int = 5
num_3 : int = 17
num_4 : int = 44
num_5 : int = 32
Printeza rezultatul averagul lui acesta numere.

3.Imparte numele tau complet in doua parti. nume_primar sa fie numele tau primar, numar_familie sa fie numala tau de familie.
E.g.
nume : str = "Ahmad Sulaibi"
nume_primar : str = nume[:5]
nume_final : str = nume[-7:]
printeaza nume_primar si nume_final separate.

4.Ai un numar si trebuie sa imi dai ultimul numar.
E.g.
numar : int = 223145821145
Sa-mi printeze numarul 5.
HINT: Foloseste Modulus (%).

5.Printeaza un patrat de 1's. Foloseste print('1' * n)
Output:
11111
11111
11111
11111
11111

6.paragraph : str = "The fox jumped from the farm"
Output:
The
fox
jumped
from
the 
farm
"""
# -----------------------------------------
"""
# Ex.1 - GOOD!
x=int(input("x="))
ecuatie= x - x*x + x*x*x*x
# alternative poti folosi puterile (**)
# exuatie = x - x**2 + x ** 4
# puterile scurteaza programul si usor
# de citit.
print(ecuatie)
"""

# -----------------------------------------

# Ex.2 - GOOD!
"""
n : int = 20
m : int = 5
p : int = 17
a : int = 44
g : int = 32
media=(n+m+p+a+g)/5
print(media)
"""

# -----------------------------------------

# Ex.3 - GOOD!
"""
nume : str="Georgiana Gabor"
prenume : str=nume[:9]
nume_familie :str=nume[-5:]
print(prenume)
print(nume_familie)
"""

# -----------------------------------------

# Ex.4 - GOOD!
"""
n=int(input("n="))
n_1=10
print(n % n_1)
"""

# -----------------------------------------

# Ex.6 - GOOD!
"""
text= "The fox jumped from the farm "
w_1=text[:3]
w_2=text[4:7]
w_3=text[8:14]
w_4=text[15:19]
w_5=text[-9:-6]
w_6=text[-5:-1]
print(w_1)
print(w_2)
print(w_3)
print(w_4)
print(w_5)
print(w_6)
"""

# -----------------------------------------

# Ex.5, poate fii aplicata folosind
# print('1'*n), astea inseamna ca
# printeaza 1 de 'n' ori. deci daca
# n = 3, printeza 111.

""" 
print('1'*5)
print('1'*5)
print('1'*5)
print('1'*5)
print('1'*5)
"""