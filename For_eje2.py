#Calcular las tablas de multiplicar del 1 hasta el 9

for n in range(1,11):
    print("--------tabla del "+str(n)+"--------")
    for x in range (1,11): # el software toma los resultados del ciclo desde 1 a 10 y lo mutliplica por n, el cual empieza en 1 y termina en 10 
        resultado = n * x #ejemplo, en el ciclo "for x" la primera iteración es x=1, esa iteración crece hasta 10 (0,1,2...10) pero n sigue valiendo n01. Cuando esto termine, se repite el ciclo para n=2
        print("El resultado es", n,"x", x, "=", resultado)
    