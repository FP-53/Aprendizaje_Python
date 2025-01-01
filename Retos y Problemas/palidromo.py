cadena = 'Aibofobia'
cadena = cadena.replace('','').lower()
if str(cadena) == "".join(reversed(cadena)):
    print("Palindromo")
else:
    print("No es Palindromo")