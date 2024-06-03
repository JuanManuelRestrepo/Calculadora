def division():
    try:
        divisor=float(input("Digite el divisor: "))
        dividendo=float(input("Digite el dividendo: "))
    except ValueError: print("Digite un valor valido")
    division=dividendo/divisor
    print(f"El resultado de la division es: {division}")
    