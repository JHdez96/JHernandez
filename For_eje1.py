
#for x in range(2,10,2):
    #print(x)

#Lo que hace el programa es repetir la operación (n*x) un total de 10 veces hasta completar el ciclo en n
n = (int(input("Ingrese un número al que desea conocer su tabla de multiplicar: ")))

for x in range(0,11):
    mult = x*n
    print ("El resultado es", n,"x", x, "=", mult)