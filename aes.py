from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message, AES.block_size))
    iv = cipher.iv
    return iv + ct_bytes

def decrypt_message(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return pt.decode()

# Example usage
key = get_random_bytes(16)  # 16 bytes key for AES-128
message = b"Hello, AES encryption!"  # Convert message to bytes
ciphertext = encrypt_message(key, message)
print("Encrypted:", ciphertext)
decrypted = decrypt_message(key, ciphertext)
print("Decrypted:", decrypted)
