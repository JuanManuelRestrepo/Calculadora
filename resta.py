def resta():
    numeros = []
    try:
        N_operadores = int(input("Digite el numero de operadores con los cuales desea operar: "))
        for i in range(N_operadores):
            num = float(input(f"Digite el operador {i+1}: "))
            numeros.append(num)
    except ValueError:
        print("Digite un valor valido")
        return  # Termina la función en caso de error para evitar más cálculos incorrectos

    if len(numeros) == 0:
        print("No se ingresaron operadores.")
        return

    resultado_resta = numeros[0]  # Inicializa con el primer número
    for num in numeros[1:]:  # Resta todos los siguientes números
        resultado_resta -= num

    print(f"El resultado de la resta es: {resultado_resta}")
    return resultado_resta
