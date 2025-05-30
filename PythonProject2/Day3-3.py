from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt
message = b"I love anime"
token = cipher.encrypt(message)

# Decrypt
original = cipher.decrypt(token)

print("Encrypted:", token)
print("Decrypted:", original)
