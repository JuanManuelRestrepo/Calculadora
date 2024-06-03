import suma
import resta
import division
import multiplicación
import exponente
print("BIENVENIDO")
desicion=int(input("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Exponente\nDigite la opcion:"))
def main():
    while True:
        try:
            if desicion==1:
                suma.suma()
                break
            elif desicion==2:
                resta.resta()
                break
            elif desicion==3:
                multiplicación.multiplicacion()
                break
            elif desicion==4:
                division.division()
                break
            elif desicion==5:
                exponente.exponentes()
            else:
                print("opcion no valida")
                break
        except ValueError:
            print("Error, ingrese un numero")

if __name__ == "__main__":
    main()
