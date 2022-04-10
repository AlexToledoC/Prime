def run():
    print("Bienvenido al programa para imprimir números pares o impares.")
    eleccion = input("¿Desea par o impar? \nEscriba su respuesta: ")
    fin = int(input("¿Hasta qué número desea consultar?: "))
    if eleccion == "par" or eleccion == "par " or eleccion == "PAR" or eleccion == "Par":
       for i in range(0, fin + 1, 2):
           print(i)
    else:
        for i in range(1, fin + 1, 2):
            print(i)


if __name__ == '__main__':
    run()