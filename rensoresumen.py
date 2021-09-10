from PIL import Image

ma = Image.open("a.png") #nombre de la imagen de la letra a
#TODO: crear las imagenes para cada letra.
#TODO: enable on production
#mA = ma.resize((n, m)) #letra mayuscula
#ma = ma.resize((c, q)) #cambiar el tamano de la letra minuscula
#TODO: determinar el size de las imagenes tanto para minuscula y mayuscula
#TODO: crear la imagen del size del texto
#TODO: calcular el size de de la imagen resultante a partir de la cantidad de letras.
def cambio(f):
    F = open(f, "r")
    i = 0
    j = 0
    lines = F.readlines()
    for line in lines:
        while i < len(F):
            while j < len(F[j]):
                if F[i][j] == "a":
                    return 