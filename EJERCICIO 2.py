class TextFormatter:
    def __init__(self, texto_original):
        self.texto_original = texto_original

    def separar_oraciones(self):
        oraciones = self.texto_original.split("#")
        return oraciones

    def capitalizar_oraciones(self, oraciones):
        oraciones_capitalizadas = [oracion.capitalize() for oracion in oraciones]
        return oraciones_capitalizadas

    def agregar_puntos(self, oraciones_capitalizadas):
        oraciones_capitalizadas[0] += "..."
        return oraciones_capitalizadas

    def agregar_bullets(self, oraciones_capitalizadas):
        oraciones_formateadas = [oraciones_capitalizadas[0]] + [f"• {oracion}." for oracion in oraciones_capitalizadas[1:-2]] + [f"• {oracion}." for oracion in oraciones_capitalizadas[-2:]]
        return oraciones_formateadas

    def formatear_texto(self, oraciones_formateadas):
        texto_formateado = "\n".join(oraciones_formateadas)
        return texto_formateado

def main():
    texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    formatter = TextFormatter(texto_original)

    oraciones = formatter.separar_oraciones()
    oraciones_capitalizadas = formatter.capitalizar_oraciones(oraciones)
    oraciones_capitalizadas = formatter.agregar_puntos(oraciones_capitalizadas)
    oraciones_formateadas = formatter.agregar_bullets(oraciones_capitalizadas)
    texto_formateado = formatter.formatear_texto(oraciones_formateadas)

    print(texto_formateado)

if __name__ == "__main__":
    main()
