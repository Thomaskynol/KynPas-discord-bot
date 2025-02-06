import datetime
import random

def generateId(prefix: str) -> str:
    checker = random.randint(1, 10)

    agora = datetime.datetime.now()
    data_str = agora.strftime("%Y%m%d%H%M%S")
    
    id_final = f"{prefix}{data_str}{checker}"
    return id_final