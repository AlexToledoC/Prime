def es_primo(numero):
    if numero == 1 or numero == 2 or numero == 3 or numero == 5 or numero == 7:
        return True
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        return False
    else:
        return True


def run():
    print("Bienvenid@ al programa para saber si un número es primo o no.")
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else: 
        print("No es primo")


if __name__ == '__main__':
    run()