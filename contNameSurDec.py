nameSur = str(input("Escreva seu nome completo (sem acentos): "))
letra = nameSur.split()
junto = ''.join(letra)

spaces = 0
letters = 0

# Listas
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
          "S", "T", "U", "V", "W", "X", "Y", "Z"]


a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

sumTotal = 0

for word in nameSur:
    if word == 'a' or word == 'A':
        sumTotal = 0 + a
    elif word == 'b' or word == 'B':
        sumTotal = 0 + b
    elif word == 'c' or word == 'C':
        sumTotal = 0 + c
    elif word == 'd' or word == 'D':
        sumTotal = 0 + d
    elif word == 'e' or word == 'E':
        sumTotal = 0 + e
    elif word == 'f' or word == 'F':
        sumTotal = 0 + f
    elif word == 'g' or word == 'G':
        sumTotal = 0 + g
    elif word == 'h' or word == 'H':
        sumTotal = 0 + h
    elif word == 'i' or word == 'I':
        sumTotal = 0 + i
    elif word == 'j' or word == 'J':
        sumTotal = 0 + j
    elif word == 'k' or word == 'K':
        sumTotal = 0 + k
    elif word == 'l' or word == 'L':
        sumTotal = 0 + l
    elif word == 'm' or word == 'M':
        sumTotal = 0 + m
    elif word == 'n' or word == 'N':
        sumTotal = 0 + n
    elif word == 'o' or word == 'O':
        sumTotal = 0 + o
    elif word == 'p' or word == 'P':
        sumTotal = 0 + p
    elif word == 'q' or word == 'Q':
        sumTotal = 0 + q
    elif word == 'r' or word == 'R':
        sumTotal = 0 + r
    elif word == 's' or word == 'S':
        sumTotal = 0 + s
    elif word == 't' or word == 'T':
        sumTotal = 0 + t
    elif word == 'u' or word == 'U':
        sumTotal = 0 + u
    elif word == 'v' or word == 'V':
        sumTotal = 0 + v
    elif word == 'w' or word == 'W':
        sumTotal = 0 + w
    elif word == 'x' or word == 'X':
        sumTotal = 0 + x
    elif word == 'y' or word == 'Y':
        sumTotal = 0 + y
    elif word == 'z' or word == 'Z':
        sumTotal = 0 + z
    elif word == ' ':
        pass
    else:
        print("ERROR: Incorrect Character")

for word in nameSur:
    for letter in letras:
        if word == letter:
            letters += 1
    if word == " ":
        spaces += 1

print("Tem", letters, "letras")
print("Tem", spaces, "espacos")
print()