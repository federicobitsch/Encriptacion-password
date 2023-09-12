#GENERADOR DE CONTRASEÑAS
import random
from werkzeug.security import generate_password_hash #generar un password encriptado

minus='abcdefghijklmnopqrstuvwxyz'

mayus=minus.upper()

numeros="0123456789"

simbolos="@();/<>#!$%&="

base=minus+mayus+numeros+simbolos

longitud = 12


for _ in range(12):
                #muestra la variable base y longitud
    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    password_encriptado=generate_password_hash(password)
    #print("{} -> {} ".format(password,password_encriptado))
        



nombre = "federico pepe nepepepe pepeppe pepe"

nombre_join = "".join(nombre)