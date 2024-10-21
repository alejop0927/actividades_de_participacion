from collections import Counter
from typing import Tuple  # Asegúrate de importar Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.contenido = []

    def leer(self):
        # Abrir el archivo en modo lectura
        with open(self.nombre_archivo, 'r') as archivo:
            # Leer el contenido del archivo línea por línea
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
            return promedio_temperatura  # Asegúrate de devolver el promedio
        else:
            print("No se encontraron temperaturas en el archivo.")
            return 0  # Retornar 0 si no hay temperaturas

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
            return promedio_humedad  # Asegúrate de devolver el promedio
        else:
            print("No se encontraron humedades en el archivo.")
            return 0  # Retornar 0 si no hay humedades
         
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
            return promedio_presion  # Asegúrate de devolver el promedio
        else:
            print("No se encontraron presiones en el archivo.")
            return 0  # Retornar 0 si no hay presiones
         
    def velocidad_promedio_viento(self):
        suma_viento = 0
        cont = 0

        for linea in self.contenido:
            if "Viento:" in linea:
                cont += 1
                viento_data = linea.split(':')[1].strip().split(',')
                velocidad = float(viento_data[0])  # Solo tomamos la velocidad
                suma_viento += velocidad

        if cont > 0:
            promedio_viento = suma_viento / cont
            print("La suma de los vientos es:", suma_viento, 'y el promedio es', promedio_viento)
            return promedio_viento  # Asegúrate de devolver el promedio
        else:
            print("No se encontraron vientos en el archivo.")
            return 0  # Retornar 0 si no hay vientos
         
    def direccion_predominante_viento(self):
        direcciones = []

        for linea in self.contenido:
            if "Viento:" in linea:
                viento_data = linea.split(':')[1].strip().split(',')
                direccion = viento_data[1].strip()  # Tomamos la dirección
                direcciones.append(direccion)

        if direcciones:
            contador_direcciones = Counter(direcciones)
            direccion_predominante = contador_direcciones.most_common(1)[0][0]  # La más común
            print(f"La dirección predominante del viento es: {direccion_predominante}")
            return direccion_predominante  # Asegúrate de devolver la dirección
        else:
            print("No se encontraron direcciones de viento en el archivo.")
            return ""  # Retornar cadena vacía si no hay direcciones

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        self.leer ()
        promedio_temperatura = self.temperatura_promedio()
        promedio_humedad = self.humedad_promedio()
        promedio_presion = self.presion_promedio()
        promedio_viento = self.velocidad_promedio_viento()
        direccion_predominante = self.direccion_predominante_viento()
        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_viento, direccion_predominante

# Ejemplo de uso
datos = DatosMeteorologicos('.txt')
datos.procesar_datos()