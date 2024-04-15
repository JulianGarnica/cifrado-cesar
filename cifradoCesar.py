import string
abecedario = list(string.ascii_lowercase)
print(string.ascii_lowercase)
opcion = input("""
¿Qué quiere hacer?
1 Cifrar
2 Descifrar

""")
texto = list(input("Inserte el texto a cifrar/descifrar "))
posT = int(input("Ingrese la contraseña "))
pos = 0
for ubic in range(posT):
    if pos > len(abecedario):
        pos = 0
    else:
        pos += 1
posTemp = 0
textoRespuesta = ""
if opcion == "1":
    for letra in texto:
        letraCif = ""
        posLetra = abecedario.index(letra)
        try:
            letraCif = abecedario[posLetra+pos]
        except:
            dif = posLetra+pos-len(abecedario)
            letraCif = abecedario[dif]
        
        textoRespuesta += letraCif
        posTemp += 1
else:
    for letra in texto:
        letraCif = ""
        posLetra = abecedario.index(letra)
        try:
            letraCif = abecedario[posLetra-pos]
        except:
            dif = posLetra+pos+len(abecedario)
            print(dif)
            letraCif = abecedario[dif]
        
        textoRespuesta += letraCif
        posTemp += 1
    
print(textoRespuesta)