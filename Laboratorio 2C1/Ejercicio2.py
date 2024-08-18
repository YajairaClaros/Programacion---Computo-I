class Articulo:
    # Atributos de clase
    nombre = ""
    marca = ""
    precio_compra = 0.0
    precio_venta = 0.0
    
    # Método constructor
    def __init__(self, nombre, marca, precio_compra):
        self.nombre = nombre
        self.marca = marca
        self.precio_compra = precio_compra
        self.calcular_precio_venta()

    # Método para calcular el precio de venta
    def calcular_precio_venta(self):
        self.precio_venta = self.precio_compra * 1.30
    
    # Método para mostrar los datos del artículo
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Marca:", self.marca)
        print("Precio de Compra:", self.precio_compra, "COP")
        print("Precio de Venta:", round(self.precio_venta, 2), "COP")
        print("*******************************")

# Subclase para cuadernos
class Cuaderno(Articulo):
    def __init__(self, hojas, precio_compra):
        super().__init__(f"Cuaderno de {hojas} hojas", "HOJITAS", precio_compra)
        self.hojas = hojas

# Subclase para lápices
class Lapiz(Articulo):
    def __init__(self, tipo, precio_compra):
        super().__init__(f"Lápiz de {tipo}", "RAYAS", precio_compra)
        self.tipo = tipo

# Crear instancias de cuadernos y lápices
cuaderno1 = Cuaderno(50, 2000)
cuaderno2 = Cuaderno(100, 3500)
lapiz1 = Lapiz("grafito", 500)
lapiz2 = Lapiz("colores", 700)

# Mostrar los datos de los artículos
cuaderno1.mostrar_datos()
cuaderno2.mostrar_datos()
lapiz1.mostrar_datos()
lapiz2.mostrar_datos()
