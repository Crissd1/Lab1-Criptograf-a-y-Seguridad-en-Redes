def cesar(text, despl):
	result = ""
	for char in text:
		if char.isupper():
			result += chr((ord(char) + despl - 65) % 26 + 65)
		elif char.islower():
			result += chr((ord(char) + despl - 97) % 26 + 97)
		else:
			result += char
	return result

if __name__== "__main__":
	text = input ("Ingresa el texto a cifrar: ")
	despl = int(input("Ingresa el valor del desplazamiento: "))
	texto_encriptado = cesar(text, despl)
	print("Texto cifrado:", texto_encriptado)
