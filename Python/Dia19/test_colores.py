from colorama import Fore, Style, init

# Inicializamos colorama
init()

print(Fore.GREEN + "¡Éxito! Estás usando una librería externa dentro de tu venv." + Style.RESET_ALL)
print(Fore.RED + "Esto no afecta al resto de tu ordenador." + Style.RESET_ALL)