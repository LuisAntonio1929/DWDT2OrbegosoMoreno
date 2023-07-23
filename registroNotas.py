from alumnos import alumnos
if __name__ == '__main__':
    print("Bienvenidos al registro de notas")
    listaAlumnos=[]
    while True:
        comando=input("Ingrese comando: ")
        if comando=="R":
            print("A continuación se le solicitará ingresas los campos para registrar a un alumno siguiendo el siguiente formato:")
            print("Nombres\nApellidos\nEdad\nNacionalidad")
            nombres=input("Ingrese el nombre del alumno")
            apellidos=input("Ingrese los apellidos del alumno")
            edad=input("Ingrese la edad del alumno")
            nacionalidad=input("Ingrese la nacionalidad del alumno")
            listaAlumnos.append(alumnos(nombres,apellidos,edad,nacionalidad))
        elif comando=="C":
            print("Ingrese la nota de cada estudiante con el siguiente formato:\n##.##")
            for i in listaAlumnos:
                while True:
                    nota=input("Alumno %s , Ingrese nota: "%(i.leerNombre()+' '+i.leerApellido()))
                    try:
                        nota=float(nota)
                    except:
                        print("Se ingresó un caracter extraño.")
                    if(0<=nota<=20):
                        i.registrarNota(nota)
                        break
                    else:
                        print("La nota debe de ser entre 0 a 20.")
        elif comando=="P":
            n=len(listaAlumnos)
            suma=sum([i.leerNota() for i in listaAlumnos])
            promedio=suma/n
            print("El promedio de notas para %i es : %f"%(n,round(promedio,2)))
        elif comando=="S":
            suma=sum([i.leerNota() for i in listaAlumnos])
            print("La suma de notas de %i es : %f"%(n,round(suma,2)))
        elif comando=="X":
            break
        else:
            print("Comando incorrecto")