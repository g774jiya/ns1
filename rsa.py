import math

# Prompt the user to input two prime numbers
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

# Compute the product of p and q (n = p*q)
n = p * q

# Compute the totient of n (phi = (p-1)*(q-1))
phi = (p - 1) * (q - 1)

# Choose an integer e such that 1 < e < phi and e is coprime to phi
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

# Compute the modular multiplicative inverse of e modulo phi (d = e^-1 mod phi)
d = pow(e, -1, phi)

# Define the encryption and decryption functions
def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Prompt the user to input a message to encrypt
message = int(input("Enter a message to encrypt (as an integer): "))

# Encrypt the message using the public key (e, n)
ciphertext = encrypt(message, e, n)
print("Encrypted message:", ciphertext)

# Decrypt the ciphertext using the private key (d, n)
decrypted_message = decrypt(ciphertext, d, n)
print("Decrypted message:", decrypted_message)

# Use Input 17 , 19 as prime number
# Use Enter a message to encrypt (as an integer): 23 or 24 or 78
# Output will show same values for Encrypted message and Decrypted Message
