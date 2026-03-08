class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Esto es una LISTA dentro de un OBJETO
        self.reparaciones = [] 
        self.mecanico_asignado = None

    def __str__(self):
        return f"{self.marca} {self.modelo} (Reparaciones: {len(self.reparaciones)})"
    
    def añadir_reparacion(self,tarea):
        if tarea in self.reparaciones:
            print("Aviso: Esa tarea ya está programada.")
        else:
            self.reparaciones.append(tarea)
    
    def asignar_mecanico(self, mecanico_obj):
        self.mecanico_asignado = mecanico_obj
    
    def generar_informe(self):
        print("--- INFORME ---")
        print(f"Coche: {self.marca} {self.modelo}")
        if self.mecanico_asignado is None:
            print("Mecánico a cargo: PENDIENTE")
        else:
            print(f"Mecánico a cargo: {self.mecanico_asignado.nombre}")
        tareas = ", ".join(self.reparaciones)
        print(f"Lista de tareas: {tareas}")
    
    def completar_reparación(self, tarea):
        if tarea in self.reparaciones:
            self.reparaciones.remove(tarea)
            print("Tarea terminada")
        else:
            print("Error: Esa tarea no estaba pendiente.")
    
    def a_diccionario(self):
        datos_guardados = {
            "marca": self.marca,
            "modelo": self.modelo,
            "tareas": self.reparaciones,
            "operario": self.mecanico_asignado.nombre if self.mecanico_asignado else "sin asignar"
        }
        return datos_guardados

class Mecanico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Mecánico {self.nombre}. Especialidad: {self.especialidad}"


# Ejercicio 1
mi_taller = {}

coche_1 = Coche("Toyota", "Corolla")
coche_2 = Coche("Ford", "Focus")

mi_taller["1234-ABC"] = coche_1
mi_taller["5555-XYZ"] = coche_2

print(mi_taller["1234-ABC"])

# Ejercicio 2
mi_coche = mi_taller.get("1234-ABC")
mi_coche.reparaciones.append("Cambio de aceite")
mi_coche.reparaciones.append("frenos")

# Ejercicio 3
print(f"Segunda reparación del coche {mi_coche.marca} {mi_coche.modelo} fue {mi_coche.reparaciones[1]}")

# Ejercicio 4
for matricula, coche in mi_taller.items():
    if coche.marca == "Toyota":
        print(f"Encontrado un Toyota con matrícula {matricula}")

# Ejercicio 5
total_reparaciones: int = 0

for coche in mi_taller.values():
    total_reparaciones += len(coche.reparaciones)

print(f"Hoy tenemos un total de {total_reparaciones} reparaciones pendientes en el taller")

# Ejercicio 6
marca = mi_taller["5555-XYZ"].marca
numero = len(mi_taller["5555-XYZ"].reparaciones)
print(f"El coche {marca} tiene {numero} reparaciones")

# Día 2
# Ejercicio 1
comp_matricula = "9999-FFF"
if comp_matricula in mi_taller.keys():
    print("El coche está en el taller.")
else:
    print("Esa matrícula no consta en nuestros registros.")

# Ejercicio 2
reparacion_nueva = "Cambio de aceite"
if reparacion_nueva in mi_taller["1234-ABC"].reparaciones:
    print("Aviso: Esa tarea ya está programada.")
else:
    mi_taller["1234-ABC"].reparaciones.append(reparacion_nueva)

# Ejercicio 3
terminado = mi_taller.pop("5555-XYZ")
print(f"Entregando el coche {terminado.marca} {terminado.modelo}.")
print("\n", mi_taller.keys())

# Día 3
# Ejercicio 3
mecanicos = {}

mec_1 = Mecanico("Pepe", "Motores")
mecanicos["pepe"] = mec_1

coche_3 = Coche("Volkswagen", "Golf")
mi_taller["9876-ZYX"] = coche_3

mi_taller["9876-ZYX"].asignar_mecanico(mecanicos["pepe"])

print(f"El mecánico de mi coche es {mi_taller["9876-ZYX"].mecanico_asignado.nombre}")

# Ejercicio 4
mi_taller["1234-ABC"].asignar_mecanico(mecanicos["pepe"])

mi_taller["1234-ABC"].generar_informe()

# Día 4
# Ejercicio 3
del mi_taller["1234-ABC"]
if "1234-ABC" in mi_taller:
    print(mi_taller["1234-ABC"])
else:
    print("Ese coche no se encuentra en nuestro taller")

