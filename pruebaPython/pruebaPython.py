from matematicas import clsOperaciones
from re import split

#esto se llama shebang y sirve para que cuando se quiera ejecutar el script en la terminal
#no se tenga que utilizar el comando python y simplemente se escriba el nombre del fichero.

#!/usr/bin/python

#La siguiente linea le indica a el sistema que estamos trabajando en utf-8 que reemplaza al 
#sistema ascii, este es mas global e incluye caracteres especiales que ascii no incluye. 



print ("Hola Mundo acción")
print ("Aquí voy aprender a realizar scripts")

#Las variables no se tienen que definir porque python utiliza un tipado dinamico por lo que sus 
#variables saben el tipo segun el valor que se le ingrese a la variable ejm:

#intVariable = 100
#strVariable = "Tipado dinamico"

# python también permite asignar variables de una forma mas corta ejm:

#strVariableCorta, intVaribleCorta, decimalVariable = "Variable corta", 200, 2.7


#para asignar numero muy grande esta el tipo de dato long que no tiene limites se asigna 
#colocando Una L al final del numero

#longVariable = 8374l

#python permite asignar valores con formato hex, dec, bin, oct

#para usar octal se coloca primero el numero cero, en el siguiente ejemplo se usa 0165
#que en decimal representa el 117
#octalVariable = 0165

#para asignar binarios se antepone 0b + numero ejm

#binarioVariable  = 0b101011

#para asignar hexadecimales, se antepone 0x ejm:

#HexadeVariable = 0xab34d

#para asignar notación cientifica se escribe la e y la potencia de 10 que necesitemos ejm:

#cientificaVariable = 12e6 # esto es igual 12 x 10 ^ 6

#asignación de booleanos, el valor debe empezar por mayuscula y el resta en minusculas
#boolVariable = True 

#asignacion de cadenas cuando ocupan mas de un renglon 

#cadenaVariable = """Como esta cadena ocupa mas de un 
#renglón por eso se 
#usa las comillas triples"""

#para que python ignore las comillas dentro de una cadena le anteponemos \

#cadenaVAriableComilla = "el dijo: \"Que los follen\""

#cadenaVAriableComilla = 'el dijo: "Que los follen"' # también se puede utilizar de esta manera

#cadenaVAriableComilla = "Que venga hace \\t \t"
#print type(cadenaVariable)
#print cadenaVAriableComilla

#Saber el tipo de la variable que se esta manejando
#strVariable = "string"

#print type(strVariable)

# convertido a diferentes tipos ejm
#innt = "10"
#print int(innt)

#strVariable = '145'
#print (int(strVariable)+10)
#print (type(strVariable))
#print (float(strVariable))

# is sirve para saber si dos objetos son el mismo 
# is not sirve para saber si dos objetos no son el mismo
#var = 100
#var1 = 100
#print (var1 is var1) #retorna true porque es el mismo elemento
#print (var is var1) #retorna false porque no es el mismo elemento
#print (var is not var) #retorna false porque es el mismo elemento
#print (var is not var1) #retorna true porque no es el mismo elemento

#El operador (in) sirve para saber si un elemento pertenece a un conjunto de elementos
#El operador (not in) sirve para saber si un elemento no pertenece a un conjunto de elementos

#list = ["silla","mesa","mantel"]
#del list[1] #esta linea borra el elemento mesa
#print (list)

#print ("silla" in list) #retorna true porque silla esta entre los elementos de list
#print ("closet" not in list) #retorna true porque silla no esta entre los elementos de list

#var = True | True 
#print (var)

#se puede crear listas dentro de una lista
#para imprimir se proporciona el indice de la sublista y luego el indice del elemento
#list = [["a",'b','c'],['1','2','3']]
#del list[1]#se borra la segunda sublista
#print (list)

#list = [3,4,5,["a",'b','c']]
#print (list[2]) #imprime el 5
#print (list)

#para obtener sublistas de una lista, desde una posicion a otra
#list = ["a",'b','c','1','2','3']
#list2 = list[0:5] # se toma desde el primer valor hasta el 5-1 = 4
#print (list2)

#para mostrar elementos de una lista saltandose posiciones de 2 en 2 o 3 en 3
#list = ["a",'b','c','1','2','3']
#list2 = list[0:6:2] # [posicion de inicio : posicion final - 1 : salto]
#print (list2)

#los diccionarios son una especie de lista donde se emparejan conceptos el primero engloba el segundo

#diccionario = {"rey":["william",'edwin'],"reina":"luisa","hijos":"mascotas"}

#print (diccionario["rey"]) #imprime william y edwin porque son el significado para rey 

#en python las varables se almacenan con un id, si asigno a una variable el valor de otra el id sera el mismo

#var = 'Qsedcfgtyh'
#var2 = 'Qsedcfgtyh'
#var1 = var
#print(id(var))
#print(id(var1)) #imprime el mismo id porque el espacio donde se almacena el valor es el mismo
#print(id(var2)) #imprime el mismo id porque el espacio donde se almacena el valor es el mismo debido a que el valor es igual
#esto es genial porque el almacenamiento es mas optimo

#var= 11234711 
#var2=11234711 
#print (id(var))
#print (id(var2))

#condicional if
#if 1 == 1:
#    print ("Prueba")
#    print ("Condicional if")
#    print ("hello")
#print ("siempre se escribe")

#condicional if con else
#if 1 == 2:
#    print ("la condicion se cumple")
#else: 
#    print ('la condicion no se cumple')

#condicional if anidado
#var = 3; var2 = 2
#if var == var2:
#    print ("se cumple la condicion")
#elif var <= var2:
#    print("var es menor o igual que var2")
#else:
#    print ("no se cumplen las condiciones")

#buble while
#var = 0
#while var < 10: 
#    var+=1
#    print (var)
 
#while con else
#while var < 4:
#    print (var)
#    var+=1
#else:
#    print("aun no se acaba")
 
# continue sirve para hacer que un buble que salte un paso y siga con los demás
#var = 0
#while var < 10:
#    var+=1
#    if var == 3:
#      continue
#    print (var)

#while para escribir las tablas del 3 - 7
#var = 1
#var1 = 3
#while var <= 7:
#    print ("Tabla del "+ str(var))
#    var1 = 1
#    while var1 <= 10:
#        print (str(var) + " x " + str(var1) )
#        var1+=1
#    var+=1

#ciclo for en python se comporta como el foreach en c#

#lista = ["a","b","c","d"]
#for letra in lista:
#    print("conforma el abc: " + letra)

#se puede hacer con cadenas 

#palabra = "William, aprende"
#for letra in palabra[:]:
#    print (letra)

#tambien se pueden recorrer diccionarios
#diccionario = {"nombre":"William","apellido":"Murillo","apellido2":"Mena"}
#for definicion in diccionario:
#    print (definicion)#este escribe nombre, apellido, apellido2

#for definicion in diccionario:
#        print (definicion + ": " + diccionario[definicion])#escribe nombre: william, apellido: Murillo

#otra forma de hacer lo mismo del anterior for es usando iteritem
#for definicion, valor in diccionario.items():
#    print (definicion + ": "+ valor)#escribe nombre: william, apellido: Murillo

#manejo de excepciones en python
#dividendo = 10
#divisor = 0
#try:
#    res = dividendo/divisor
#except:
#    if divisor == 0:
#        print("No se puede divir entre 0")

#para manejar excepciones especificamente
#dividendo = "A"
#divisor = 2
#try:
#    res = dividendo/divisor
#except ZeroDivisionError:
#    print ("No se puede divide entre 0")
#except TypeError:
#    print ("no se puede dividir cadenas con números")


#leer un numero y mostrar si es primo 
#try:
#    print ("Ingresa un numero para saber si es primo")
#    res = int(input())
#    var = 2
#    cont = 0
#    while var < res:
#        if res % var == 0:
#            cont+=1
#            if cont >= 2:
#                break
#        var+=1
#    if cont == 0:
#        print ("Es un numero primo")
#    else:
#        print ("No es un numero primo") 
#except:
#    print ('Ingrese un numero entero')

#funciones en python
#def fnSaludar():
#    print("Hola, esta es una funcion en python")
#fnSaludar()

#funciones que devuelven valores
#def fnObtenerSuma():
#    return 4 + 3
#print (fnObtenerSuma())

#funciones con parametros
#def fnDividir(numA, numB):
#    try:
#        res = numA/numB
#        return res
#    except:
#        return "No se puede hacer esta división"
#print (fnDividir(2,4))

#python permite asignar valores a variables por defecto en las funciones
#def fnSumar(num, num2 = 3):
#    return num+num2
#print (fnSumar(3,6))

#cuando no se sabe cuantos parametro vamos a recibir podemos hacer lo siguiente
#def fnSumar(*numeros):
#    res = 0
#    for numero in numeros:
#        res+= numero
#    return res
#print (fnSumar(1,2,3,4,5,6,7,2))#retorna 30


#comentarios docstring (documentacion string)
"""
De esta forma se comenta el codigo usando varias lineas
"""

#YELD sirve para ir retornando valores en el momento en el que se obtengan, esto optimiza recuersos
#def fnObtenerLista():
#    var = 1
#    while var <=10:
#        yield var
#        var+=1
#for num in fnObtenerLista():
#     print(num)

#Los decoradores son funciones dentro de otro funcion 

#def decorador(fnEntrada):
#    def fnSalida():
#        print ("Esto lo agrega la funcion en el decorador")
#        fnEntrada()
#    return fnSalida
#@decorador
#def fnQueEntra():
#    print("Esto lo agrega la funcion que entra")
#fnQueEntra()

"""
Las funciones tipo lambda permiten crear funciones de forma mas corta
siempre retornan el valor de su resultado sin usar return
"""

#fnSumar = lambda: 2+3#funcion sin parametros
#print (fnSumar()) #retorna 5

#fnsumar = lambda x,y: x **y #funcion lambda con parametros retorna x elevado a la y
#print(fnsumar(3,4))#retorna 81

#===================================================================================
"""
Trabajando con POO
para heredar al definir la clase se coloca entre parentesis class(Clase_A_Heredar, Clase_A_Heredar2 )
"""
"""
class animal:

    #constructor
    def __init__(self,Nombre, Patas):
       self.nombre = Nombre
       self.patas = Patas

    def mtInfoAminal(self):
        print("El " + self.nombre + " tiene "+ str(self.patas) + " patas")
       
miAnimal = animal("Perro",4)
miAnimal2 = animal("Gallo",2)
miAnimal.mtInfoAminal()
miAnimal2.mtInfoAminal()
"""
#===================================================================================

""""
#Esto sirve para ver las rutas donde hay archivos .py y asi saber que puedo importar y demás
import sys
print (sys.path)

"""
"""
Las siguientes líneas creo un paquete llamado matematicas, luego creo una clase operaciones que contiene 
la operación de la suma, para poder usar este paquete, su clase y sus metodos se hace los siguiente
"""
"""
import matematicas.clsOperaciones as ope #asigno un alias para no usar todo el camino

objOperaciones = ope.clsOperaciones()#instancio el objeto

objOperaciones.mtSumar(2,7)#ejecuto el metodo que retorna 9
"""

"""
#voy a instanciar una clase que esta en el mismo paquete, es decir en la misma carpeta

#objOpera = clsOperaciones.clsOperaciones()
#objOpera.mtSumar(2,4)

"""

"""
formato de cadenas
%s para agregar string
%d para agregar enteros
%x para agregar hexadecimal
%e para notación exponencial
%o para agregar octal
%f enteros con decimales

var =  "este texto se agrega"
print ("Hola %s."% var  )

print ("Hola %s %s %s %s " %("william","heriti","fucc", "fer"))

#para dejar espacios antes o despues de la cadena 

print ("Hola %20s %-10s -" % ("william","murillo") )

#para agregar numero enteros se usa %d en lugar de %s

print("La edad de %s es de %d  años" %("William",20))

var = 1000

print("Numero en decimal: %d, Octal %o, Hexadecimal %x, exponecial %e .decimal %f" %(var,var,var,var, var/43))
"""
"""
var = input("Escriba su nombre ")

print ("Hola "+ var)
"""


#interfax grafica
"""
import tkinter

principal = tkinter.Tk()

texto = tkinter.Label(principal, text= "Hola mundo")
texto.pack()
principal.mainloop()
"""
"""
#abrir archivos desde el script, en este caso un .txt se muestra todo su contenido
fichero = open("texto.txt","r")
print ("Este es el contenido del fichero .txt") 
print (fichero.read())#muestra todo el contenido del archivo
print (fichero.readline())#muestra línea por línea

fichero.close()#cierro el fichero optimizando espacio
"""
"""
fichero = open("texto.txt","w")
print ("Ingresa nuevo texto para el fichero .txt")
fichero.write(input())
fichero.close()

fichero = open("texto.txt","r")
print ("Este es el nuevo contenido del fichero .txt")
print (fichero.read())
fichero.close()
"""
"""
print ("probando scripts desde la consola")
print ("Ingrese dos numeros para sumarlos")
import matematicas.clsOperaciones as ope
objOperar = ope.clsOperaciones()

print (objOperar.mtSumar(input("Ingrese numA: "),input("Ingrese numB: ")))
"""

"""
import random
print ("Numero aleatorio entre 0.0 y 1.0 con ramdom.ramdom(): " + str(random.random()))
print ("Numero aleatorio entre 2 y 3 con ramdom.randint(2,30): " + str(random.randint(2,30)))

#numero aleatorio desde un secuencia
import random
lista = [2,3,4,5]
print(random.choice(lista))

"""
"""
fichero = open("texto.txt", "r")# r indica abierto en modo lectura
fichero2 = open("texto.txt", "r")

print (fichero.read())
cont = 0
for i in fichero2:
   cont+=1#cuento las líneas del fichero

print ("Este archivo tiene " + str(cont) + " líneas")

fichero.close()
fichero2.close()
"""

"""
#Aquí voy a agregar una imagen dentro de un tkinter que es la GUI 
from tkinter import *
marco = tkinter.Tk() #asigna el marco principal GUI
marco.title("Mostrando imagen en una gui") #asigno un título
label = Label(marco, Image =imagen).pack()arco.mainloop()
#imagen.close()#cierro la imagen
"""

def fnSumar(numeros):
    for caso in numeros: #recorre todas las sublistas dentro de la lista principal
        total = 0
        yield int(caso[1]) + int(caso[0]) #En casa ciclo de la secuencia retorna la suma

casos = int(input()) #Leo la primera línea con el número de casos
listaMaestra = []
for caso in range(casos): #Recorre todas las líneas con los casos
    listaMaestra.append(input().split()) # anexo a la lista principal sublistas con los dos valores de cada línea

#print (fnSumar(listaMaestra))
for caso in fnSumar(listaMaestra): #llamo la fnSumar que retorna una secuencia, la recorro y escribo sus valores
   print(caso)