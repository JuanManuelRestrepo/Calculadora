resultado=0
def exponentes():
    try:
        base=float(input("Digite la base"))
        exponente=float(input("Digite el exponente"))
    except ValueError: print("Digite un valor valido")
    resultado_exponente=base**exponente
    print(f"El resultado de la operacion es: {resultado_exponente}")
 
