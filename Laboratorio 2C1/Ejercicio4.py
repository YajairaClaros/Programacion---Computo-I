class Dispositivo:
    # Atributos de clase
    nombre = ""
    modelo = ""
    tamaño_pantalla = 0.0
    memoria = 0
    color = ""
    precio_compra = 0.0
    precio_venta = 0.0
    
    # Atributos fijos
    marca = "PHR"
    es_importado = True

    # Método constructor
    def __init__(self, nombre, modelo, tamaño_pantalla, memoria, color, precio_compra):
        self.nombre = nombre
        self.modelo = modelo
        self.tamaño_pantalla = tamaño_pantalla
        self.memoria = memoria
        self.color = color
        self.precio_compra = precio_compra
        self.calcular_precio_venta()

    # Método para calcular el precio de venta
    def calcular_precio_venta(self):
        self.precio_venta = self.precio_compra * 1.7
    
    # Método para mostrar los datos del dispositivo
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Modelo:", self.modelo)
        print("Tamaño de Pantalla:", self.tamaño_pantalla, "pulgadas")
        print("Memoria:", self.memoria, "GB")
        print("Color:", self.color)
        print("Precio de Compra:", self.precio_compra)
        print("Precio de Venta:", round(self.precio_venta, 2))
        print("Marca:", self.marca)
        print("Importado:", "Sí" if self.es_importado else "No")
        print("*******************************")

# Función para ingresar los datos del dispositivo
def registrar_dispositivo():
    nombre = input("Nombre del dispositivo (Celular, Tablet, Portátil): ")
    modelo = input("Modelo del dispositivo: ")
    tamaño_pantalla = float(input("Tamaño de la pantalla (en pulgadas): "))
    memoria = int(input("Memoria del dispositivo (en GB): "))
    color = input("Color del dispositivo: ")
    precio_compra = float(input("Precio de compra del dispositivo: "))

    return Dispositivo(nombre, modelo, tamaño_pantalla, memoria, color, precio_compra)

# Registrar dispositivos
print("Registrar dispositivo")
dispositivo1 = registrar_dispositivo()


# Mostrar los datos de los dispositivos registrados
print("---------------------------------------")
print("       DATOS DEL DISPOSITIVO")
print("---------------------------------------")
dispositivo1.mostrar_datos()

