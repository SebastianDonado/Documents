import math
def xcuadrado(x,y):
    z = x**y
    ##print(f"Este es el resultado de la función {z}")
    return z

##xcuadrado(x= int (input("ingrese el valo de x \n")), y= int (input("ingrese el valo de y \n")))

def area_circulo(r):
   ## area = math.pi * (r**2)
    area = math.pi * xcuadrado(r,2)
    print(f"El area del circulo con radio {r} en metros es de {area}m")

area_circulo(r = int(input("Ingrese el valor del radio del circulo en metros \n")))