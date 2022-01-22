#@profsandromesquita
import serial

try:
    conectado = serial.Serial("COM14", 115200, timeout=0.5)
    #print(conectado)
    print("Conectado com a porta", conectado.portstr)
except serial.SerialException:
    print("Porta USB não detectada!")
    pass

while True:
    comando = input("Digita L para ligar ou D para desligar:")
    if comando == "L":
        conectado.write(b'1')
    else:
        conectado.write(b'0')
    if input("Deseja continuar?").upper()=="N":
        break

conectado.close()
print("Conexão fechada")
