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

aa = '1'
bb = '2'
cc = '3'
dd = '4'
ee = '5'
ff = '6'
gg = '7'
hh = '8'
ii = '9'
jj = '10'
kk = '11'
ll = '12'
mm = '13'
nn = '14'
oo = '15'
pp = '16'
qq = '17'
rr = '18'
ss = '19'
tt = '20'
uu = '21'
vv = '22'
ww = '23'
xx = '24'
yy = '25'
zz = '26'

sumTotal = 0
nameNum = ''

for word in nameSur:
    if word == 'a' or word == 'A':
        sumTotal = sumTotal + a
        nameNum = nameNum + aa
    elif word == 'b' or word == 'B':
        sumTotal = sumTotal + b
        nameNum = nameNum + bb
    elif word == 'c' or word == 'C':
        sumTotal = sumTotal + c
        nameNum = nameNum + cc
    elif word == 'd' or word == 'D':
        sumTotal = sumTotal + d
        nameNum = nameNum + dd
    elif word == 'e' or word == 'E':
        sumTotal = sumTotal + e
        nameNum = nameNum + ee
    elif word == 'f' or word == 'F':
        sumTotal = sumTotal + f
        nameNum = nameNum + ff
    elif word == 'g' or word == 'G':
        sumTotal = sumTotal + g
        nameNum = nameNum + gg
    elif word == 'h' or word == 'H':
        sumTotal = sumTotal + h
        nameNum = nameNum + hh
    elif word == 'i' or word == 'I':
        sumTotal = sumTotal + i
        nameNum = nameNum + ii
    elif word == 'j' or word == 'J':
        sumTotal = sumTotal + j
        nameNum = nameNum + jj
    elif word == 'k' or word == 'K':
        sumTotal = sumTotal + k
        nameNum = nameNum + kk
    elif word == 'l' or word == 'L':
        sumTotal = sumTotal + l
        nameNum = nameNum + ll
    elif word == 'm' or word == 'M':
        sumTotal = sumTotal + m
        nameNum = nameNum + mm
    elif word == 'n' or word == 'N':
        sumTotal = sumTotal + n
        nameNum = nameNum + nn
    elif word == 'o' or word == 'O':
        sumTotal = sumTotal + o
        nameNum = nameNum + oo
    elif word == 'p' or word == 'P':
        sumTotal = sumTotal + p
        nameNum = nameNum + pp
    elif word == 'q' or word == 'Q':
        sumTotal = sumTotal + q
        nameNum = nameNum + qq
    elif word == 'r' or word == 'R':
        sumTotal = sumTotal + r
        nameNum = nameNum + rr
    elif word == 's' or word == 'S':
        sumTotal = sumTotal + s
        nameNum = nameNum + ss
    elif word == 't' or word == 'T':
        sumTotal = sumTotal + t
        nameNum = nameNum + tt
    elif word == 'u' or word == 'U':
        sumTotal = sumTotal + u
        nameNum = nameNum + uu
    elif word == 'v' or word == 'V':
        sumTotal = sumTotal + v
        nameNum = nameNum + vv
    elif word == 'w' or word == 'W':
        sumTotal = sumTotal + w
        nameNum = nameNum + ww
    elif word == 'x' or word == 'X':
        sumTotal = sumTotal + x
        nameNum = nameNum + xx
    elif word == 'y' or word == 'Y':
        sumTotal = sumTotal + y
        nameNum = nameNum + yy
    elif word == 'z' or word == 'Z':
        sumTotal = sumTotal + z
        nameNum = nameNum + zz
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

print("\nTem", letters, "letras.")
print("Tem", spaces, "espacos.")
print("A soma de suas letras sao", sumTotal, "no total.")
print("Nome numerico sem soma de numeros:", nameNum)