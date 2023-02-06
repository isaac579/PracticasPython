print("***************************************************")
print(" Sitema para detectar si es mayor o menor el numero")
print("***************************************************")

numero_uno = int(input("Ingresa el primer numero."))
numero_dos = int(input("Ingresa el segundo numero."))
numero_tres = int(input("Ingresa el tercer numero."))

if numero_uno > numero_dos & numero_uno > numero_tres:
    print("El numero ",numero_uno," Es el numero mas grande de los tres.")
else:
    if numero_dos > numero_uno & numero_dos > numero_tres:
        print("El numero ",numero_dos," Es el numero mas grande de los tres.")
    else:
        print("El numero ",numero_tres," Es el numero mas grande de los tres.")