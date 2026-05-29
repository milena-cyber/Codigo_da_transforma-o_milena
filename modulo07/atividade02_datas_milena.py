from datetime import datetime

agora = datetime.now()

print("Data atual:")

print(agora.strftime("%d/%m/%Y"))

print("Hora atual:")

print(agora.strftime("%H:%M:%S"))