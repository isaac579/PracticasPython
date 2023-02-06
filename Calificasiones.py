print("**********************************************")
print("Sistema para saber el promedio de las materias, y si estas aprobado o no")
print("**********************************************")

nombre_alumno = input("Ingresa el nombre del alumno.")
matematicas = float(input("Ingresa tu calificasion para matematicas."))
fisica = float(input("Ingresa tu calificasion para fisica."))
quimica = float(input("Ingresa tu calificasion para quimica."))

promedio = (matematicas + fisica + quimica)/3

if promedio >= 6:
    print("Felicidades ",nombre_alumno, " Has aprobado con un promedio de: ",promedio)
else:
    print(nombre_alumno," Lamentablemente has reprobado, con un promedio de: ",promedio)
