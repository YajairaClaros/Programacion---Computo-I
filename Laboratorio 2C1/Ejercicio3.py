class Vehiculo:
    # Atributos de clase
    marca = ""
    modelo = ""
    año = 0
    color = ""
    numero_puertas = 0
    precio_compra = 0.0
    precio_venta = 0.0
    nacionalidad = ""
    placa = ""
    transmision = ""
    combustible = ""
    
    # Atributos fijos por ley
    ruedas = 4
    capacidad_pasajeros = 5

    # Método constructor
    def __init__(self, marca, modelo, año, color, numero_puertas, precio_compra, nacionalidad, placa, transmision, combustible):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.numero_puertas = numero_puertas
        self.precio_compra = precio_compra
        self.nacionalidad = nacionalidad
        self.placa = placa
        self.transmision = transmision
        self.combustible = combustible
        self.calcular_precio_venta()

    # Método para calcular el precio de venta
    def calcular_precio_venta(self):
        self.precio_venta = self.precio_compra * 1.4
    
    # Método para mostrar los datos del vehículo
    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Color:", self.color)
        print("Número de Puertas:", self.numero_puertas)
        print("Precio de Compra:", self.precio_compra, "COP")
        print("Precio de Venta:", round(self.precio_venta, 2), "COP")
        print("Nacionalidad:", self.nacionalidad)
        print("Placa:", self.placa)
        print("Transmisión:", self.transmision)
        print("Combustible:", self.combustible)
        print("Ruedas:", self.ruedas)
        print("Capacidad de Pasajeros:", self.capacidad_pasajeros)
        print("*******************************")

# Función para ingresar los datos del vehículo
def registrar_vehiculo():
    marca = input("Marca del vehículo: ")
    modelo = input("Modelo del vehículo: ")
    año = int(input("Año del vehículo: "))
    color = input("Color del vehículo: ")
    numero_puertas = int(input("Número de puertas: "))
    precio_compra = float(input("Precio de compra del vehículo: "))
    nacionalidad = input("Nacionalidad (Nacional o Importado): ")
    placa = input("Placa del vehículo: ")
    transmision = input("Tipo de transmisión (Manual o Automática): ")
    combustible = input("Tipo de combustible (Gasolina, Diesel, Eléctrico, etc.): ")

    return Vehiculo(marca, modelo, año, color, numero_puertas, precio_compra, nacionalidad, placa, transmision, combustible)

# Registrar vehículo
print("Registrar vehículo")
vehiculo1 = registrar_vehiculo()


# Mostrar los datos de vehículo registrado
print("---------------------------------------")
print("         DATOS DEL VEHICULO")
print("---------------------------------------")
vehiculo1.mostrar_datos()

