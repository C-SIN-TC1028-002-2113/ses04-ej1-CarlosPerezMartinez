def main():
    #escribe tu código abajo de esta línea
    edad=int(input("Ingresa tu edad: "))
    if edad>=18 and edad<=120:
        licencia=input("¿Tienes identificación oficial? (s/n): ")
        if licencia=="s":
            print("Trámite de licencia concedido")
        elif licencia=="n":
            print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif edad<0 or edad>120:
        print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")

if __name__ == '__main__':
    main()
