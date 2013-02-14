# --------------- Universidad de los Andes ---------------
# ---------------   Fisica computacional   ---------------
# Tarea 2 - 2013 I
# Autor:
#       Andres Felipe Garcia Albarracin - 201012816

# Librerias
import sys

# Funciones
def letraValida(var):
    if var == ",": return False
    elif var == ";": return False
    elif var == ".": return False
    elif var == " ": return False
    elif var == "\n": return False
    elif var == "\r": return False
    elif var == "\xa0": return False
    elif var == "\xad": return False
    elif var == ":": return False
    elif var == "'": return False    
    elif var == "(": return False
    elif var == ")": return False
    elif var == "[": return False
    elif var == "]": return False
    elif var == "{": return False
    elif var == "}": return False
    else: return True


# Tomar los archivos de entrada
a = len(sys.argv)

if (a != 2):
    print "Revise los parametros de entrada"
    sys.exit(1)

nombreArchivo = sys.argv[1]

# Vectores usados en el algoritmo
vectorCaracteres = []
vectorRepeticiones = []

# Leer el archivo dado por parametro
archivo = open(nombreArchivo,'r')

#totalCaracteres = len(archivo.read())
while 1:
    var = archivo.read(1)
    existe = 0          # Para determinar si la letra ya existe en vectorCaracteres
    if var == "":
        break           # En caso de que se termine de leer el archivo
    if (letraValida(var)):
        for i in range(len(vectorCaracteres)):
            if var == vectorCaracteres[i]:
                existe = 1
                vectorRepeticiones[i] = vectorRepeticiones[i] + 1
        if (existe == 0):
            vectorCaracteres = vectorCaracteres + [var]
            vectorRepeticiones = vectorRepeticiones + [1]

if (len(vectorCaracteres) != len(vectorRepeticiones)):
    print "ERROR los vectores no son identicos"
    sys.exit(1)

# Organizacion de los vectores
# Organizacion por medio del algoritmo de seleccion
listaRecorrido = range(len(vectorCaracteres))
for i in range(len(vectorCaracteres)-1):
    posMayor = i
    cantidadMayor = vectorRepeticiones[i]
    letraMayor = vectorCaracteres[i]
    for j in listaRecorrido[i:]:
        if (vectorRepeticiones[j] > cantidadMayor):
            cantidadMayor = vectorRepeticiones[j]
            letraMayor = vectorCaracteres[j]
            posMayor = j
    vectorCaracteres[posMayor] = vectorCaracteres[i]
    vectorRepeticiones[posMayor] = vectorRepeticiones[i]
    vectorCaracteres[i] = letraMayor
    vectorRepeticiones[i] = cantidadMayor

# Calculo del procentaje
numeroCaracteres = len(vectorCaracteres)
totalCaracteres = sum(vectorRepeticiones)
vectorPorcentajes = range(len(vectorCaracteres))
for i in listaRecorrido:
    vectorPorcentajes[i] = float(vectorRepeticiones[i])/totalCaracteres*100

# Creacion del archivo de salida
nombreArchivoSalida = "frecuencias_" + nombreArchivo
archivoSalida = open(nombreArchivoSalida,'w')
listaRecorrido = range(len(vectorCaracteres))
for i in listaRecorrido:
    lineaTexto = '%s      %.5f %s\n' % (vectorCaracteres[i], vectorPorcentajes[i], chr(0x25))
    archivoSalida.write(lineaTexto)
archivoSalida.close()

# Creacion del archivo con comentarios
nombreArchivoComentario = "comentario.txt"
archivoComentario = open(nombreArchivoComentario,'w')
lineaTexto = "Comentarios sobre la lectura del texto: %s\n" (nombreArchivo)
archivoComentario.write(lineaTexto)

print vectorCaracteres
print "El numero de caracteres es: ", numeroCaracteres
