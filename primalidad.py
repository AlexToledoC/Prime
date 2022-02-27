def es_primo(numero):
    contador = 0
    
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    print("Bienvenid@ al programa para saber si un número es primo o no.")
    numero = int(input("Escribe un número: "))
    if numero == 1:
        print("El número 1 no es primo.")
    elif es_primo(numero):
        print("Es primo")
    else: 
        print("No es primo")


if __name__ == '__main__':
    run()