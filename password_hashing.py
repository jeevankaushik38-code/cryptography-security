
import bcrypt

# Sample password for this demonstration only
password = b"Lab-Only-Example-Password-2026"

# Generate a salted bcrypt hash
salt = bcrypt.gensalt(rounds=12)
password_hash = bcrypt.hashpw(password, salt)

print("Bcrypt password hashing demonstration")
print("Work factor:", 12)
print("Password hashed successfully:", password_hash != password)
print("Stored hash:", password_hash.decode())

# Verify the correct password
correct_password = bcrypt.checkpw(password, password_hash)
print("Correct password accepted:", correct_password)

# Verify an incorrect password
wrong_password = b"Incorrect-Example-Password"
wrong_result = bcrypt.checkpw(wrong_password, password_hash)
print("Incorrect password rejected:", not wrong_result)