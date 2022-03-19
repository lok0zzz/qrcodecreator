import string
import random

characters = list(string.ascii_letters + string.digits)

random.shuffle(characters)

def gerarValorRandomico():
    string = []
    for i in range(6):
        string.append(random.choice(characters))

    final = "".join(string)
    return final
