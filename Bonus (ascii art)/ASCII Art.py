import pyfiglet
import os
import platform

user_input = input("Entrez le texte à convertir en ASCII Art : ")

current_os = platform.system()
if current_os == "Windows":
    os.system("cls")
elif current_os in ("Linux", "Darwin"):
    os.system("clear")

print(pyfiglet.figlet_format(user_input, font="graffiti"))