# -UTN-TUPaDProgramacion1-
Tarea Luciano NIcolas Ibañez probando cositas
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo")

#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla

Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = input("Ingrese su edad: ")
Lugar = input("Ingrese su lugar de residencia actualmente: ")

print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Lugar}")

#4)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = int(input("Ingrese los segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos son {horas} hora/s")

#5)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro
Radio = float(input("Ingrese el radio de su círculo: "))
pi = 3.1416

perimetro = 2 * pi * Radio
Area = pi * Radio**2

print(f"El perímetro de su círculo es {perimetro} y el área es {Area}")

#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

Numero =int(input("Ingrese Su numero para recibir las tablas "))
Resultado1 = Numero*1
Resultado2 = Numero*2
Resultado3 = Numero*3
Resultado4 = Numero*4
Resultado5 = Numero*5
Resultado6 = Numero*6
Resultado7 = Numero*7
Resultado8 = Numero*8
Resultado9 = Numero*9
Resultado10 = Numero*10
print(f"su Numero Multiplicado por 1 es:{Resultado1}")
print(f"Su Numero Multiplicado por 2 es:{Resultado2}")
print(f"Su Numero Multiplicado por 3 es:{Resultado3}")
print(f"Su Numero Multiplicado por 4 es:{Resultado4}")
print(f"Su Numero Multiplicado por 5 es:{Resultado5}")
print(f"Su Numero Multiplicado por 6 es:{Resultado6}")
print(f"Su Numero Multiplicado por 7 es:{Resultado7}")
print(f"Su Numero Multiplicado por 8 es:{Resultado8}")
print(f"Su Numero Multiplicado por 9 es:{Resultado9}")
print(f"Su Numero Multiplicado por 10 es:{Resultado10}")

#7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
Numero1 = int(input("Ingrese su Primer Numero"))
Numero2 = int(input("Ingrese su Segundo Numero"))
Suma = Numero1 + Numero2
Resta = Numero1 - Numero2
Multiplicacion = Numero1 * Numero2
Division = Numero1 / Numero2
print(f"Sus 2 Numeros sumados dan: {Suma} ")
print(f"Sus 2 Numeros restados dan: {Resta}")
print(f"Sus 2 Numeros Multiplicados dan: {Multiplicacion}")
print(f"Sus 2 Numeros Divididos dan: {Division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

Peso = int(input("Ingrese su Peso en Kg "))
Altura =float(input("Ingrese su altura en Metros "))
Masacorporal= Peso/Altura**2
print(f"Su Indice de masa corporal es de: {Masacorporal}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

Celsius =int(input("Ingrese la temperatura en grado Celcius "))
Fahrenheit = Celsius*9/5+32
print(f"Su temperatura en Fahrenheit equivale a: {Fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
Numero1 = int(input("Ingrese su Primer Numero "))
Numero2 = int(input("Ingrese su Segundo Numero "))
Numero3 = int(input("Ingrese su Tercer Numero "))
Promedio=(Numero1+Numero2+Numero3)/3
print(f"El Promedio de sus 3 Numeros es {Promedio}")