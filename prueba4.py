import ovito.io as ov
import ovito.data as ovd
import numpy as np

# Función de búsqueda en profundidad para encontrar clústeres
def dfs(particle_index, visited, cluster, finder, neighbor_count, umbral_vecinos_1, umbral_vecinos_2):
    stack = [particle_index]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            cluster.add(current)
            for neigh in finder.find(current):
                if neighbor_count[neigh.index] <= umbral_vecinos_1 or neighbor_count[neigh.index] > umbral_vecinos_2:
                    stack.append(neigh.index)

# Importar archivo LAMMPS
pipeline = ov.import_file("/home/emil/Documentos/lammps/Plantilla_colocar_particulas2.lammpstrj")
data = pipeline.compute()

# Definir el cutoff para el vecino
cutoff = 1.3
finder = ovd.CutoffNeighborFinder(cutoff, data)

# Inicializar un diccionario para realizar un seguimiento del número de vecinos
neighbor_count = {}

# Umbrales de vecinos
umbral_vecinos_1 = 3
umbral_vecinos_2 = 7

# Lista para almacenar los índices de las partículas que cumplen con las condiciones
potential_particles = []

# Loop sobre todas las partículas
for index in range(data.particles.count):
    current_neighbor_count = 0

    # Iterar sobre los vecinos de la partícula actual
    for neigh in finder.find(index):
        # Incrementar el contador de vecinos para la partícula actual
        current_neighbor_count += 1

    # Actualizar el recuento total para el índice actual en el diccionario
    neighbor_count[index] = current_neighbor_count

    # Verificar si el recuento de vecinos es menor al primer umbral o mayor al segundo umbral
    if current_neighbor_count <= umbral_vecinos_1 or current_neighbor_count > umbral_vecinos_2:
        potential_particles.append(index)
# Calcular el número total de vecinos y el promedio de vecinos por partícula
total_neighbors = sum(neighbor_count.values())
average_neighbors_all_particles = total_neighbors / data.particles.count
# Encontrar el clúster que contiene las partículas seleccionadas
visited = set()
cluster = set()
if potential_particles:
    # Iniciar la búsqueda de clústeres desde la primera partícula que cumple la condición
    dfs(potential_particles[0], visited, cluster, finder, neighbor_count, umbral_vecinos_1, umbral_vecinos_2)

# Guardar información del tipo y posición de las partículas que cumplen la condición en el mismo clúster
if cluster:
    with open("selected_particles_info2.txt", "w") as output_file:
        for selected_index in cluster:
            particle_type = data.particles['Particle Type'][selected_index]
            position = data.particles['Position'][selected_index]
            output_file.write(f"{selected_index} {particle_type} {position[0]} {position[1]} {position[2]}\n")
    print(f"Se ha creado el archivo 'selected_particles_info2.txt'.")
else:
    print("No hay partículas que cumplan la condición.")

print("NUMBER OF ATOMS WITH LESS THAN 4 NEIGHBORS:", sum(1 for i in cluster if neighbor_count[i] <= umbral_vecinos_1))
print("NUMBER OF ATOMS WITH MORE THAN 7 NEIGHBORS:", sum(1 for i in cluster if neighbor_count[i] > umbral_vecinos_2))
print(f"The average number of neighbors for all particles is {average_neighbors_all_particles:.2f}.")
