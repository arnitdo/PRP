characterConstant = 'A'
print(" A =", ord(characterConstant))

numericConstant = 81
print("81 =", hex(numericConstant))
print("81 =", oct(numericConstant))
print("81 =", bin(numericConstant))

hexadecimalStringConstant = "0x3A"
octalStringConstant = "0o75"
binaryStringConstant = "0b001011"

hexadecimalValue = int(hexadecimalStringConstant, 16)
octalValue = int(octalStringConstant, 8)
binaryValue = int(binaryStringConstant, 2)

print(hexadecimalStringConstant, "=", hexadecimalValue)
print(octalStringConstant, "=", octalValue)
print(binaryStringConstant, "=", binaryValue)

zeroCharacter = 48
print(f"ASCII value of {zeroCharacter} is '{chr(zeroCharacter)}'")
