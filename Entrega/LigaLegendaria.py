import os
import json
# Ingresando


def saludar():
    print("BIENVENIDO A LA LIGA DE LAS LEGENDAS")


saludar()
# Preguntar
option = int(input("1) Para crearte una cuenta \n2) Si ya tenes cuenta \n-"))
datos = {}
datos["invocadores"] = []
os.system("cls")

if (option == 1):
    print("Hora de registrarnos\n")
    name = input("Nombre de Invocador: ")
    email = input("Correo: ")
    pwd = input("Contraseña: ")

    file = open("./Entrega/Invocadores/invocadores.json", "a")
    file.write(f"{name}|{pwd}|{email}\n")
    file.close()
    print("Registro Exitoso!")
elif (option == 2):
    print("INICIAR SESION\n")
    name = input("Nombre de Invocador: ")
    pwd = input("Contraseña: ")
    os.system("cls")
    file = open("./Entrega/Invocadores/invocadores.json", "r")
    for line in file.readlines():
        data = line.split("|")
        if (data[0] == name and data[1] == pwd):
            print(f"Ingresando a la Liga de las Legendas {data[0]}")
            print("Listo para perder PL?")
            file.close()
            break
    else:
        print("Este invocador no existe :(")
