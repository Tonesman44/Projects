def encryptChar(letter, shift):
    # starts in range 97 to 122, want to move to range 0-25
    asciiVal = ord(letter) #97 - 122
    letterVal = asciiVal - ord("a") #0 -25
    encryptedVal = (letterVal + shift) % 26
    encryptedLetter = chr(encryptedVal + ord("a"))
    return encryptedLetter
ciphertext = 'dzeevjfkrlezkvuwffksrcctcls'                          
  
for shift in range(0,26):
    plaintext = ""
    for letter in ciphertext:
        plaintext += encryptChar(letter,shift)
    print(26-shift, plaintext)

#17
