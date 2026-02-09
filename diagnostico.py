import os
import sys
import platform
import getpass # Importamos este nuevo módulo

def mostrar_diagnostico():
    # Esta versión es más compatible con terminales de VS Code y Linux
    usuario = getpass.getuser()
    
    sistema = platform.system()
    version_py = sys.version.split()[0]
    info = sys.version_info
    
    print("-" * 30)
    print(f"¡Hola, {usuario}! Bienvenida/o a Python.")
    print("-" * 30)
    print(f"S.O. Detectado: {sistema}")
    print(f"Versión de Python: {info.major}.{info.minor}.{info.micro}")
    print(f"Ruta del archivo: {os.path.abspath(__file__)}")
    print("-" * 30)

if __name__ == "__main__":
    mostrar_diagnostico()