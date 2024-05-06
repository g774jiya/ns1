from random import randint

# Shared prime number and base
p = int(input("Enter A Prime Number")) # Prime number
g = int(input("Enter A number such that 1<g<p"))  # Generator

# Alice's private key
a_private = randint(2, p - 2)  # Random private key for Alice

# Bob's private key
b_private = randint(2, p - 2)  # Random private key for Bob

# Calculate public keys
a_public = pow(g, a_private, p)  # (g ^ a) mod p
b_public = pow(g, b_private, p)  # (g ^ b) mod p

# Exchange public keys
shared_key_a = pow(b_public, a_private, p)  # (B_public ^ a_private) mod p
shared_key_b = pow(a_public, b_private, p)  # (A_public ^ b_private) mod p

# Both should have the same shared key
print("Shared Key (Alice):", shared_key_a)
print("Shared Key (Bob):", shared_key_b)
