import serial
conexao = ""

try:
    conexao = serial.Serial("COM11", 9600, timeout=0.5)
    print("Conectado na porta: ", conexao.portstr)
except serial.SerialException:
    pass
if conexao != "":
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")