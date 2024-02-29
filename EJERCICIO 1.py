import math

class Estrella:
    def __init__(self, nombre, x=0, y=0, z=0):
        """
        Constructor de la clase Estrella.

        :param nombre: Nombre de la estrella.
        :param x: Coordenada x en el espacio tridimensional.
        :param y: Coordenada y en el espacio tridimensional.
        :param z: Coordenada z en el espacio tridimensional.
        """
        self.nombre = nombre
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """
        Método para obtener la representación en cadena de la estrella.

        :return: Cadena que representa la estrella.
        """
        return f"{self.nombre} en ({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        """
        Método para determinar la galaxia en la que podría estar ubicada la estrella.

        :return: Nombre de la galaxia.
        """
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia A"
        elif self.x < 0 and self.y < 0 and self.z < 0:
            return "Galaxia B"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        """
        Método para calcular la distancia entre dos estrellas en el espacio 3D.

        :param otra_estrella: Otra instancia de la clase Estrella.
        :return: Distancia entre las dos estrellas.
        """
        dx = self.x - otra_estrella.x
        dy = self.y - otra_estrella.y
        dz = self.z - otra_estrella.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

# Experimentación
estrella_A = Estrella("Estrella A", 2, 3, 1)
estrella_B = Estrella("Estrella B", 4, 4, 4)
estrella_C = Estrella("Estrella C", -3, -1, 0)

# Imprimir información de las estrellas y sus galaxias
print(estrella_A)
print(estrella_B)
print(estrella_C)
print(f"Galaxia de A: {estrella_A.galaxia()}")
print(f"Galaxia de B: {estrella_B.galaxia()}")
print(f"Galaxia de C: {estrella_C.galaxia()}")

# Calcular distancias entre estrellas
dist_AB = estrella_A.distancia(estrella_B)
dist_BC = estrella_B.distancia(estrella_C)
dist_AC = estrella_A.distancia(estrella_C)  # Nueva línea para calcular la distancia entre A y C
print(f"Distancia entre A y B: {dist_AB:.2f}")
print(f"Distancia entre B y C: {dist_BC:.2f}")
print(f"Distancia entre A y C: {dist_AC:.2f}")

# Encontrar la estrella más lejana del origen y mostrar información
origen = Estrella("Origen")
estrellas = [estrella_A, estrella_B, estrella_C]
estrella_mas_lejana = max(estrellas, key=lambda estrella: estrella.distancia(origen))
print(f"La estrella más lejana del origen es {estrella_mas_lejana.nombre} con una distancia de {estrella_mas_lejana.distancia(origen):.2f}")
