class alumnos:
    def __init__(self,nombre,apellidos,edad,nacionalidad):
        self.nombre = nombre
        self.apellidos =apellidos
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.nota = 0
    def leerNota(self):
        return self.nota
    def registrarNota(self,notaAlumno):
        self.nota = notaAlumno
    def leerNombre(self):
        return self.nombre
    def leerApellido(self):
        return self.apellidos
    def leerNacionalidad(self):
        return self.nacionalidad
    