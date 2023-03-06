
"""FUNCIONES DE AYUDA"""
import re
import os
import platform

def clear():
    """Limpia la pantalla"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def matricula_valida(matricula, lista): 
    if not re.match('[0-9]{2}[A-Z]$', matricula):
        print("Matrícula incorrecta, debe cumplir el formato.")
        return False
    for vehiculo in lista:
        if vehiculo.matricula == matricula:
            print("Matrícula utilizada por otro vehículo.")
            return False
    return True
        