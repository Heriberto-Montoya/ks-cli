import os
import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyStoreManager:
    def __init__(self, master_password):
        self.vault_path = "vault.dat"
        self.salt_path = "salt.key"
        self.master_password = master_password.encode()
        self.key = self._derive_key()
        self.fernet = Fernet(self.key)

    def _derive_key(self):
        # Generar o cargar la sal (salt) para el KDF
        if os.path.exists(self.salt_path):
            with open(self.salt_path, "rb") as f:
                salt = f.read()
        else:
            salt = os.urandom(16)
            with open(self.salt_path, "wb") as f:
                f.write(salt)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        return base64.urlsafe_b64encode(kdf.derive(self.master_password))

    def _read_vault(self):
        if not os.path.exists(self.vault_path):
            return {}
        try:
            with open(self.vault_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = self.fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data)
        except Exception:
            print("Error: Contraseña incorrecta o archivo de datos corrupto.")
            exit(1)

    def _write_vault(self, data):
        encrypted_data = self.fernet.encrypt(json.dumps(data).encode())
        with open(self.vault_path, "wb") as f:
            f.write(encrypted_data)

    def add_credential(self, name, username, password):
        vault = self._read_vault()
        vault[name] = {"user": username, "password": password, "type_key": "credential"}
        self._write_vault(vault)
        return vault[name]

    def add_note(self, title, content):
        vault = self._read_vault()
        vault[title] = {"content": content, "type_key": "note"}
        self._write_vault(vault)
        return vault[title]

    def list(self):
        vault = self._read_vault()
        return vault
        # if not vault:
        #     print("La bóveda está vacía.")
        #     return

        # print("\n--- Credenciales Almacenadas ---")
        # print(f"{'Servicio':<20} | {'Usuario':<20} | {'Contraseña':<20}")
        # print("-" * 65)
        # for service, info in vault.items():
        #     print(f"{service:<20} | {info['user']:<20} | {info['pass']:<20}")
