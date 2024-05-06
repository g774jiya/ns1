from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA

# Generate RSA keys
key = RSA.generate(2048)

# Prompt the user to input a message to sign
message = input("Enter a message to sign: ")

# Hash the message using SHA-1
hashed_message = SHA.new(message.encode())

# Sign the hashed message using the private key
signature = pkcs1_15.new(key).sign(hashed_message)

# Print the signature in hexadecimal format
print("Signature (hex):", signature.hex())

# Prompt the user to input a message to verify
verified_message = input("Enter a message to verify: ")

# Hash the verified message using SHA-1
hashed_verified_message = SHA.new(verified_message.encode())

# Verify the signature using the public key
try:
    pkcs1_15.new(key.publickey()).verify(hashed_verified_message, signature)
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is invalid.")
