# RSA Algorithm Simplified
p, q, e = 3, 11, 7  # Example prime numbers and public exponent
n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)  # Private exponent

# Encryption and Decryption
encrypt = lambda msg: pow(msg, e, n)
decrypt = lambda cipher: pow(cipher, d, n)

# Example Usage
msg = 4  # Example message
cipher = encrypt(msg)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher))
