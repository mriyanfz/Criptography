def encrypt(text,s):
    result = ""
 # transversal teks biasa
    for i in range(len(text)):
        char = text[i]
 # Enkripsi karakter huruf besar dalam teks biasa
        if (char.isupper()):
             result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.isnumeric()):
             result += chr((ord(char) + s-48) % 10 + 48)
        elif (ord(char) >=33 and ord(char) <=47):
             result += chr((ord(char) + s-33) % 14 + 33)
 # Enkripsi karakter huruf kecil dalam teks biasa
        else:
             result += chr((ord(char) + s - 97) % 26 + 97)
    return result
#periksa fungsi di atas
text = input(" Text Encryption Chyper : ")
s = 4
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))