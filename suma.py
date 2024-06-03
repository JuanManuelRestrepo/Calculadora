def suma():
    try:
        numeros=[]
        N_operadores=(input("Digite el numero de operadores con los cuales desea operar:"))
        for i in range(int(N_operadores)):
            num=float(input(f"Digite el operador {i+1}: "))
            numeros.append(num)
    except ValueError: 
        print("Digite un valor valido")
    resultado_suma=0
    for i in range(len(numeros)):
        resultado_suma= resultado_suma + numeros[i]
    print(f'El resultado de la suma es: {resultado_suma}')
    