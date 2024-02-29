#Texto original
#un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro

texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Separar las oraciones utilizando el símbolo '#' como delimitador
oraciones = texto_original.split("#")

# Capitalizar la primera letra de cada oración
oraciones_capitalizadas = [oracion.capitalize() for oracion in oraciones]

# Agregar "..." al final de la primera oración
oraciones_capitalizadas[0] += "..."

# Agregar bullets (viñetas) y punto al final solo a las últimas tres frases
oraciones_formateadas = [oraciones_capitalizadas[0]] + [f"• {oracion}." for oracion in oraciones_capitalizadas[1:-2]] + [f"• {oracion}." for oracion in oraciones_capitalizadas[-2:]]

# Unir las oraciones con un salto de línea
texto_formateado = "\n".join(oraciones_formateadas)

print(texto_formateado)
