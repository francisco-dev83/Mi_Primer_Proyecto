# Declaración de la cuenta
cuenta: dict[str, int] = {"saldo": 1000}

#lógica del coódigo
def main():
    while cuenta["saldo"] > 0:
        try:
            reintegro = int(input("Introduce la cantidad de dinero que quieres sacar(0 para salir): "))
        except ValueError:
            print("Debes introducir un número entero.")
        else:
            if reintegro == 0:
                break
            elif reintegro < 0:
                print("No puedes retirar cantidades negativas.")
            elif reintegro > cuenta["saldo"]:
                print("Saldo insuficiente.")
            else:
                cuenta["saldo"] = cuenta["saldo"] - reintegro
        finally:
            print(f"Saldo en cuenta: {cuenta['saldo']}")

    print("--- Gracias por utilizar nuestro servicio ---")

if __name__ == "__main__":
    main()