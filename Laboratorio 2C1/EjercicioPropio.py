'''Un estudiante quiere tener una agenda donde pueda llevar todo en orden. 
Haz que tenga por lo menos 5 caracteristicas'''


class Agenda:
    # Atributos de clase
    titulo = ""
    descripcion = ""
    fecha = ""
    hora = ""
    lugar = ""
    prioridad = ""
    
    # Método constructor
    def __init__(self, titulo, descripcion, fecha, hora, lugar, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.prioridad = prioridad
    
    # Método para mostrar los datos de una tarea/evento
    def mostrar_tarea(self):
        print("Título:", self.titulo)
        print("Descripción:", self.descripcion)
        print("Fecha:", self.fecha)
        print("Hora:", self.hora)
        print("Lugar:", self.lugar)
        print("Prioridad:", self.prioridad)
        print("*******************************")

# Función para registrar una tarea/evento
def registrar_tarea():
    titulo = input("Título de la tarea/evento: ")
    descripcion = input("Descripción de la tarea/evento: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    lugar = input("Lugar del evento: ")
    prioridad = input("Prioridad (Alta, Media, Baja): ")

    return Agenda(titulo, descripcion, fecha, hora, lugar, prioridad)


# Registrar tarea
print("Registrar tarea")
tarea1 = registrar_tarea()


# Mostrar los datos de los dispositivos registrados
print("---------------------------------------")
print("              AGENDA")
print("---------------------------------------")
tarea1.mostrar_tarea()

