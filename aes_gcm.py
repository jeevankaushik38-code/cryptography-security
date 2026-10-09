
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

# Generate a random 256-bit (32-byte) encryption key
key = AESGCM.generate_key(bit_length=256)

# Generate a fresh, random 96-bit nonce
nonce = os.urandom(12)

# Sample message for demonstration only
message = b"Task 05: Cryptography demonstration"

# Create the AES-GCM cipher
aesgcm = AESGCM(key)

# Encrypt the message
ciphertext = aesgcm.encrypt(nonce, message, None)

# Decrypt the message and verify its authenticity
plaintext = aesgcm.decrypt(nonce, ciphertext, None)

# Display results
print("AES-256-GCM demonstration")
print("Original message:", message.decode())
print("Decrypted message:", plaintext.decode())
print("Encryption and decryption successful:", plaintext == message)
print("Nonce (Base64):", base64.b64encode(nonce).decode())
print("Ciphertext (Base64):", base64.b64encode(ciphertext).decode())
print("Authentication verification: successful")
print("Note: The encryption key stays in memory and is not saved.")