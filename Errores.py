"""#Manejo de errores

num_a=1
num_b=2

try:
    div=num_a/num_b

except ZeroDivisionError:
   print("error en el programa, división entre cero")

finally: 
   print("yo siempre aparezco")
   

print("Aquí termina mi programa")


#Raise: Sirve para lanzar (de forma intencional) excepciones en Python



while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")"""


def divide (x,y):
    try:
        z= x/y
        if z < 0:
            raise ValueError("Sorry, no nunbers below zero")
        
    except (ZeroDivisionError, TypeError):
        try:
            v = 1/"a"
        except TypeError:
            print("Sorry, not possible")
    except ValueError as Ve: #Apodo
        print(Ve)

    else:
        return z
    finally:
        print("Always executed")


result=divide(12,-1)
print(result)