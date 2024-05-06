def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            cipher_text += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            cipher_text += char
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            plain_text += chr((ord(char.lower()) - ord('a') - shift + 26) % 26 + ord('a'))
            key_index += 1
        else:
            plain_text += char
    return plain_text

# Example usage:
text = "Hello, world!"
key = "key"
encrypted_text = vigenere_encrypt(text, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
