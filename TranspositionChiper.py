#L200200168

def encrypt(plaintext, key):
    # create the cipher text
    cipher_text = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            cipher_text[col] += plaintext[pointer]
            pointer += key
    return ''.join(cipher_text)

def decrypt(ciphertext, key):
    # create the plain text
    plain_text = [''] * (len(ciphertext) // key)
    for col in range(key):
        pointer = col
        for row in range(len(ciphertext) // key):
            plain_text[row] += ciphertext[pointer]
            pointer += key
    return ''.join(plain_text)

plaintext = "Desty Fitriah Murtiwari"
key = 6
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)