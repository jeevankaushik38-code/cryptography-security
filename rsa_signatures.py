
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate an RSA 2048-bit key pair for this demonstration
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Sample message to sign
message = b"Task 05: RSA digital signature demonstration"

# Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verification: successful")
except InvalidSignature:
    print("Signature verification: failed")

print("RSA key size: 2048 bits")
print("Signature algorithm: RSA-PSS with SHA-256")
print("Signature length:", len(signature), "bytes")

# Demonstrate that a modified message fails verification
try:
    public_key.verify(
        signature,
        b"Modified message",
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Modified message verification: unexpectedly successful")
except InvalidSignature:
    print("Modified message verification: correctly rejected")