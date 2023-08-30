import os
import time
import random

while True:
    title = "Piedra, Papel o Tijera".center(30, "=")
    print("==============================".center(100, " "))
    print("==============================".center(100, " "))
    print("==============================".center(100, " "))
    print("==============================".center(100, " "))
    print(title.center(100, " "))
    print("==============================".center(100, " "))
    print("==============================".center(100, " "))
    print("==============================".center(100, " "))
    print("==============================".center(100, " "))
    print("")
    print("")
    print("")
    
    print("Elegi una de las 3 opciones")
    lista = ["Piedra", "Papel", "Tijera"]
    print("1.Piedra")
    print("2.Papel")
    print("3.Tijera")
    while True:
        try:
            Avalor = int(input("Escribe el número de la opción elegida aquí: "))
            if Avalor > 0 and Avalor < 4:
                break
            else:
                print("Error")
        except ValueError:
            print("Error")
    Avalor = Avalor-1
    decicion = lista.copy()[Avalor]
    
    time.sleep(0.9)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("ahora el programa elegira entre")
    time.sleep(.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Piedra".center(100, " "))
    time.sleep(.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Papel".center(100, " "))
    time.sleep(.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("O Tijera".center(100, " "))
    
    opciones = ["Piedra", "Papel", "Tijera"]
    valorz = random.randint(0, 2)
    opcion_final = opciones[valorz]
    
    print(f"tu elegiste {decicion}")
    time.sleep(1)
    print(f"Y la maquina elegio {opcion_final}")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    if Avalor == 0 and valorz == 0:
        print("Empate")
    elif Avalor == 0 and valorz == 1:
        print("Tu perdiste, la maquina gano")
    elif Avalor == 0 and valorz == 2:
        print("Tu ganaste, la maquina perdio")
    elif Avalor == 1 and valorz == 0:
        print("Tu ganaste, la maquina perdio")
    elif Avalor == 1 and valorz == 1:
        print("Empate")
    elif Avalor == 1 and valorz == 2:
        print("Tu perdiste, la maquina gano")
    elif Avalor == 2 and valorz == 0:
        print("Tu perdiste, la maquina gano")
    elif Avalor == 2 and valorz == 1:
        print("Tu ganaste, la maquina perdio")
    elif Avalor == 2 and valorz == 2:
        print("Empate")

    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        opc = input("Quiere volver a ejecutar el programa (y/n): ")
        if opc.lower() == "y" or opc.lower() == "n":
            break
        else:
            print("Error")
    if opc == "n":
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
print("Gracias por usar el programa")