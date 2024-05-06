from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_message(key, message):
    cipher = DES.new(key, DES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(message.encode(), DES.block_size))
    return ct_bytes

def decrypt_message(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    pt = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return pt.decode()

# Example usage
key = get_random_bytes(8)  # 8 bytes key for DES
message = "Hello, DES encryption!"
ciphertext = encrypt_message(key, message)
print("Encrypted:", ciphertext)
decrypted = decrypt_message(key, ciphertext)
print("Decrypted:", decrypted)
