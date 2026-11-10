import time

tempo = int(input("digite o tempo em segundos:"))

for i in range(tempo, 0, -1):
    segundos = i % 60
    minutos = int(i / 60) % 60
    horas = (int(i / 3600))
    print("{:02}:{:02}:{:02}").format(horas, minutos, segundos)
    time.sleep(1)

    print("o tempo acabou!")

    
   

