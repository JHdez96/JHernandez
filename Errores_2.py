def IMC(peso, altura):
    try:
        resultado = round(peso / altura**2, 2)
        return resultado
        if altura >= 0:
           raise ZeroDivisionError ("No se puede dividir entre cero")
    except:
        resultado

    

def validacion(resultado):
    if resultado >= 18.5 and resultado <= 24.7:
        print("Persona saludable")
    elif resultado >= 25:
        print("Persona con sobrepeso")
 

Peso = int(input("Ingrese su peso (kg): "))
Altura = float(input("Ingrese su altura (m): "))

resultado_IMC = IMC(Peso, Altura)
print("Su IMC es:", resultado_IMC)
(validacion(resultado_IMC))



