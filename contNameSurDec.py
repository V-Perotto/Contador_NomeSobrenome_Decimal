nameSur = str(input("Escreva seu nome completo (sem acentos): "))
letra = nameSur.split()
junto = ''.join(letra)
inverso = ''

spaces = 0
letters = 0

# Listas
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
valores = []

#for letters in letras:
#    if letras[letters] == a:

for word in nameSur:
    for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
        if word == letter:
            letters += 1
    if word == " ":
        spaces += 1


print("Tem", letters,"letras")
print("Tem", spaces,"espacos")