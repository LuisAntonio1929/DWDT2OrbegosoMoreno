from alumnos import alumnos
if __name__ == '__main__':
    print("Bienvenidos al registro de notas")
    listaAlumnos=[]
    while True:
        comando=input("Ingrese comando: ")
        print()
        if comando=="R":
            print("A continuación se le solicitará ingresas los campos para registrar a un alumno siguiendo el siguiente formato:")
            print("Nombres\nApellidos\nEdad\nNacionalidad\n")
            nombres=input("Ingrese el nombre del alumno: ")
            apellidos=input("Ingrese los apellidos del alumno: ")
            while True:
                edad=input("Ingrese la edad del alumno: ")
                try:
                    edad=float(edad)
                    break
                except:
                    print("La edad debe de ser un número.")
            nacionalidad=input("Ingrese la nacionalidad del alumno: ")
            listaAlumnos.append(alumnos(nombres,apellidos,edad,nacionalidad))
        elif comando=="C":
            print("Ingrese la nota de cada estudiante con el siguiente formato:\n##.## (2 cifras significativas o se redondeará)\n")
            for i in listaAlumnos:
                while True:
                    nota=input("Alumno %s , Ingrese nota: "%(i.leerNombre()+' '+i.leerApellido()))
                    try:
                        nota=float(nota)
                        if(0<=nota<=20):
                            i.registrarNota(round(nota,2))
                            break
                        else:
                            print("La nota debe de ser entre 0 a 20.")
                    except:
                        print("Se ingresó un caracter extraño.")
        elif comando=="P":
            n=len(listaAlumnos)
            suma=sum([i.leerNota() for i in listaAlumnos])
            promedio=suma/n
            print("El promedio de notas para %i es : %.2f"%(n,promedio))
        elif comando=="S":
            suma=sum([i.leerNota() for i in listaAlumnos])
            print("La suma de notas de %i es : %.2f"%(n,round(suma,2)))
        elif comando=="X":
            break
        else:
            print("Comando incorrecto")
        print()