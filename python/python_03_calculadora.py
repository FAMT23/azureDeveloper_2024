import sys

#num1 = int(input("Inserte el número 1: "))
#num2 = int(input("Inserte el número 2: "))
#operador = input("Inserte el operador: ")

num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
operador = int(sys.argv[2])


if num1.is_integer() and num2.is_integer():
    if(operador=="*" or operador == "/" or operador=='+' or operador=="-"):
        if (operador =="*"):
            print(num1*num2)
        elif operador =="/":
            print(num1/num2)
        elif operador =="+":
            print(num1+num2)
        elif operador =="-":
            print(num1-num2)
    else:
        print("Operador indicado no válido, solo puede ser '*' '/' '+' '-' ", )
else:
    print("Alguno de los números no es válido")