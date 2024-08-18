class Perro():
    # Atributos de clase
    nombre = ""
    raza = ""
    edad = 0
    peso = 0.0
    tamaño = ""
    color = ""
    estado = "NO ATENDIDO"
    dueño = ""
    
    # Método constructor
    def __init__(self, nombre, raza, edad, peso, color, dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.estado = "NO ATENDIDO"
        self.asignar_tamaño()  # Asignar el tamaño basado en el peso

    # Método para asignar tamaño basado en el peso
    def asignar_tamaño(self):
        if self.peso < 10:
            self.tamaño = "Perro Pequeño"
        else:
            self.tamaño = "Perro Grande"

    # Método para registrar al perro y cambiar su estado
    def registrar_perro(self):
        self.estado = "ATENDIDO"
    
    # Método para mostrar los datos del perro
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Raza:", self.raza)
        print("Edad:", self.edad, "años")
        print("Peso:", self.peso, "kg")
        print("Tamaño:", self.tamaño)
        print("Color:", self.color)
        print("Dueño:", self.dueño)
        print("Estado:", self.estado)
        print("*******************************")

# Creación de instancias y registro de perros
perro1 = Perro("Max", "Labrador", 5, 15.0, "Marrón", "Juan Pérez")
perro2 = Perro("Bella", "Chihuahua", 3, 2.5, "Blanco", "Ana García")

# Registrar los perros
perro1.registrar_perro()
perro2.registrar_perro()

# Mostrar los datos de los perros
perro1.mostrar_datos()
perro2.mostrar_datos()

