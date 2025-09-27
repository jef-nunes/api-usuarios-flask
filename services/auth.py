import hashlib
import jwt
from datetime import datetime, timedelta
import os

def _get_secret_key()->str:
    return os.getenv("SECRET_KEY")

# Verifica se uma senha de input, corresponde a uma senha no banco de dados
def verify_password(password: str, hash_hex: str, salt_hex: str) -> bool:
    
    salt = bytes.fromhex(salt_hex)

    hash_bytes = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    
    return hash_bytes.hex() == hash_hex


# Gerar um token JWT
def generate_jwt(user_id: int, expires_in: int = 6000) -> str:

    payload = {
        "user_id": user_id,
        "exp": datetime.now()+timedelta(seconds=expires_in)
    }

    token = jwt.encode(payload=payload,key=_get_secret_key(),algorithm="HS256")

    return token