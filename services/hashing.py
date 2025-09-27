import hashlib, os

# Gerar um hash para uma senha
def hash_password(password: str, salt: bytes = None):
    if not salt:
        salt=os.urandom(16)
        password_bytes = password.encode("utf-8")
        hash_bytes = hashlib.pbkdf2_hmac("sha256", password_bytes, salt, 100000)
        return hash_bytes.hex(), salt.hex()