# crypto_utils.py
# Шифрование onto16r-излучения в зависимости от уровня доверия контекста
# Соответствует принципу: "энергия не встраивается в продукт, но защита — обязательна"

import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def derive_key_from_context(context_trust_level: str, salt: bytes = None) -> tuple[bytes, bytes]:
    """
    Генерирует ключ на основе уровня доверия контекста.
    Уровни: 'low', 'medium', 'high', 'vma' (high-stakes, требует VMA-подписи).
    """
    if salt is None:
        salt = os.urandom(16)
    
    trust_seed = {
        'low': b"public_context",
        'medium': b"semi_trusted_domain",
        'high': b"verified_synthetic_environment",
        'vma': b"ethically_audited_space"
    }.get(context_trust_level, b"unknown_trust")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(trust_seed))
    return key, salt

def encrypt_onto16r(onto16r_payload: str, context_trust_level: str) -> dict:
    """
    Шифрует onto16r-излучение с ключом, привязанным к уровню доверия.
    Возвращает: { 'ciphertext': ..., 'salt': ..., 'trust_level': ... }
    """
    key, salt = derive_key_from_context(context_trust_level)
    f = Fernet(key)
    ciphertext = f.encrypt(onto16r_payload.encode('utf-8'))
    return {
        "ciphertext": base64.b64encode(ciphertext).decode('ascii'),
        "salt": base64.b64encode(salt).decode('ascii'),
        "trust_level": context_trust_level
    }

def decrypt_onto16r(encrypted_package: dict) -> str:
    """
    Расшифровывает onto16r-излучение.
    """
    salt = base64.b64decode(encrypted_package["salt"])
    key, _ = derive_key_from_context(encrypted_package["trust_level"], salt=salt)
    f = Fernet(key)
    ciphertext = base64.b64decode(encrypted_package["ciphertext"])
    return f.decrypt(ciphertext).decode('utf-8')