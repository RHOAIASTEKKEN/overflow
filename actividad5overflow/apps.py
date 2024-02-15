import sys
import math
import random

# Función que causa un desbordamiento al agotar la pila de llamadas recursivas
def recursive_overflow(depth):
    while True:
        print(f"Profundidad actual de recursión: {depth}")
        depth += 1
        if depth % 1000 == 0:
            print("Profundidad actual:", depth)

# Función que causa un desbordamiento al crear un gran número de objetos
def object_overflow(count):
    objects = []
    for _ in range(count):
        objects.append(" " * 1024)  # Crear objetos grandes para consumir memoria
    object_overflow(count + 1)

# Función que causa un desbordamiento al exceder la capacidad de memoria asignada
def memory_overflow():
    data = bytearray(1024 * 1024 * 1024)  # Crear un objeto grande que consume memoria
    memory_overflow()

# Función que causa un desbordamiento al saturar el procesador
def cpu_overflow():
    while True:
        # Método de Monte Carlo para calcular Pi
        inside_circle = 0
        total_points = 0
        for _ in range(1000000):
            x = random.random()
            y = random.random()
            distance = math.sqrt(x**2 + y**2)
            if distance <= 1:
                inside_circle += 1
            total_points += 1
        pi_estimate = 4 * inside_circle / total_points

if __name__ == "__main__":
    # Descomenta una de las siguientes líneas para provocar el desbordamiento correspondiente
    
    recursive_overflow(0)  # Desbordamiento por pila de llamadas recursivas
    object_overflow(0)  # Desbordamiento por creación de objetos
    memory_overflow()  # Desbordamiento por consumo excesivo de memoria
    cpu_overflow()  # Desbordamiento por uso excesivo de CPU
