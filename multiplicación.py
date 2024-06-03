def multiplicacion():
    numeros=[]
    try:
        N_operadores=int(input("Digite el numero de operadores a utilizar: "))
        for i in range((N_operadores)):
            num=float(input(f"Digite el operador {i+1}: "))
            numeros.append(num)
    except ValueError: print("Digite un valor valido")
    resultado=numeros[0]
    for num in numeros[1:]:  
        resultado=resultado*num
    print(f"El resultado de la multiplicacion es: {resultado}")
    
    