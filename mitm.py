def decifrar_cesar(text):

    resultados = []

    for shift in range(0, 26):
        descifrado = ""
        for char in text:
            if char.isupper():
                descifrado += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                descifrado += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                descifrado += char
        resultados.append((shift, descifrado))

    return resultados
    
def resaltar_probable(text):
    palabras_clave = ["criptografía", "seguridad", "redes"]
    text = text.lower()

    for palabra in palabras_clave:
        if palabra in text:
            return True
    return False

if __name__ == "__main__":
    texto_cifrado = "larycxpajorj h bnpdarmjm nw anmnb"
    posibles_descifrados = decifrar_cesar(texto_cifrado)
    
    for shift, descifrado in posibles_descifrados:
        if resaltar_probable(descifrado):
            print(f"\033[92mDesplazamiento {shift}: {descifrado}\033[0m")
        else:
            print(f"Desplazamiento {shift}: {descifrado}")

