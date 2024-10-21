from collections import Counter
from typing import Tuple

class DatosMeteorologicos:
    DIRECCIONES_VIENTO = {
        "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
        "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
        "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
        "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
    }

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.contenido = []

    def leer(self):
        with open(self.nombre_archivo, 'r') as archivo:
            self.contenido = archivo.readlines()

    def temperatura_promedio(self):
        suma_temperatura = 0
        cont = 0

        for linea in self.contenido:
            if "Temperatura:" in linea:
                cont += 1
                temperatura = float(linea.split(':')[1].strip())
                suma_temperatura += temperatura

        if cont > 0:
            promedio_temperatura = suma_temperatura / cont
            print("La suma de las temperaturas es:", suma_temperatura, 'y el promedio es', promedio_temperatura)
            return promedio_temperatura
        else:
            print("No se encontraron temperaturas en el archivo.")
            return 0

    def humedad_promedio(self):
        suma_humedad = 0
        cont = 0

        for linea in self.contenido:
            if "Humedad:" in linea:
                cont += 1
                humedad = float(linea.split(':')[1].strip())
                suma_humedad += humedad

        if cont > 0:
            promedio_humedad = suma_humedad / cont
            print("La suma de las humedades es:", suma_humedad, 'y el promedio es', promedio_humedad)
            return promedio_humedad
        else:
            print("No se encontraron humedades en el archivo.")
            return 0

    def presion_promedio(self):
        suma_presion = 0
        cont = 0

        for linea in self.contenido:
            if "Presion:" in linea:
                cont += 1
                presion = float(linea.split(':')[1].strip())
                suma_presion += presion

        if cont > 0:
            promedio_presion = suma_presion / cont
            print("La suma de las presiones es:", suma_presion, 'y el promedio es', promedio_presion)
            return promedio_presion
        else:
            print("No se encontraron presiones en el archivo.")
            return 0

    def velocidad_promedio_viento(self):
        suma_viento = 0
        cont = 0

        for linea in self.contenido:
            if "Viento:" in linea:
                cont += 1
                viento_data = linea.split(':')[1].strip().split(',')
                velocidad = float(viento_data[0])
                suma_viento += velocidad

        if cont > 0:
            promedio_viento = suma_viento / cont
            print("La suma de los vientos es:", suma_viento, 'y el promedio es', promedio_viento)
            return promedio_viento
        else:
            print("No se encontraron vientos en el archivo.")
            return 0

    def direccion_predominante_viento(self):
        direcciones = []

        for linea in self.contenido:
            if "Viento:" in linea:
                viento_data = linea.split(':')[1].strip().split(',')
                direccion = viento_data[1].strip()
                direcciones.append(direccion)

        if direcciones:
            contador_direcciones = Counter(direcciones)
            direccion_predominante = contador_direcciones.most_common(1)[0][0]
            print(f"La dirección predominante del viento es: {direccion_predominante}")
            return direccion_predominante
        else:
            print("No se encontraron direcciones de viento en el archivo.")
            return ""

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        self.leer()
        promedio_temperatura = self.temperatura_promedio()
        promedio_humedad = self.humedad_promedio()
        promedio_presion = self.presion_promedio()
        promedio_viento = self.velocidad_promedio_viento()
        direccion_predominante = self.direccion_predominante_viento()
        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_viento, direccion_predominante

# Ejemplo de uso
datos = DatosMeteorologicos('C:/Users/apena/OneDrive/Documents/actividades_de_participacion_poo/actividad9/datos.txt')
resultados = datos.procesar_datos()
print(resultados)
