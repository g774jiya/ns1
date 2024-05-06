import hashlib

def generate_sha1_hash(message):
    sha1_hash = hashlib.sha1(message).hexdigest()
    return sha1_hash

# Example usage
message = input("Enter a Message to Hash: ")
message_bytes = message.encode("UTF-8")
sha1_hash = generate_sha1_hash(message_bytes)
print("SHA-1 Hash:", sha1_hash)
