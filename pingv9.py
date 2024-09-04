from scapy.all import IP, ICMP, send, Raw
import struct
import time
import random

def modo_stealth(texto):
    ip_destino = "8.8.8.8"
    identificador = random.randint(0, 0xFFFF)
    seq_num = 1

    for char in texto:

        timestamp_seconds = int(time.time()) & 0xFFFFFFFF
        timestamp_milliseconds = int((time.time() % 1) * 1000 ) & 0xFFFFFFFF

        datos = struct.pack("!I", timestamp_seconds) + struct.pack("!I", timestamp_milliseconds) + char.encode()

        packet = IP(dst=ip_destino)/ICMP(id=identificador, seq=seq_num)/Raw(load=datos)
        send(packet)
        print(f"Enviando carácter: {char} con seq={seq_num} y timestamp {timestamp_seconds}.{timestamp_milliseconds}")
        seq_num += 1
if __name__ == "__main__":
    texto_encriptado = "larycxpajorj h bnpdarmjm nw anmnb"
    modo_stealth(texto_encriptado)
