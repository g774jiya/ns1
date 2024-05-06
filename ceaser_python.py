def caesar_cipher(text, shift):
    encrypted = ""
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            encrypted += char
            decrypted += char
    return encrypted, decrypted

# Example usage:
plaintext = "Hello, World!"
shift_amount = 3
encrypted_text, decrypted_text = caesar_cipher(plaintext, shift_amount)
print("Original:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
