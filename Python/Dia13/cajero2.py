from banco_logica import procesar_retiro

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
            if reintegro < 0:
                print("No puedes retirar cantidades negativas.")
                continue
            
            nuevo_saldo = procesar_retiro(cuenta["saldo"], reintegro)

            if nuevo_saldo is None:
                print("Saldo insuficiente.")
                continue

            cuenta["saldo"] = nuevo_saldo
            print("Retiro realizado: ")

        finally:
            print(f"Saldo en cuenta: {cuenta['saldo']}")

    print("--- Gracias por utilizar nuestro servicio ---")

if __name__ == "__main__":
    main()