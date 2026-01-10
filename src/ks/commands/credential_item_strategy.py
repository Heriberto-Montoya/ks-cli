from ks.keystore.keystore_manager import KeyStoreManager
from .item_strategy import ItemStrategy

class CredentialItemStrategy(ItemStrategy):    
    def create(self, ks_manager: KeyStoreManager, name: str, args):
        user = getattr(args, 'user', None)
        if not user:
            raise ValueError("User is required for credential type")
        
        # Solicitar contraseña de forma segura
        password = args.password
        if not password:
            raise ValueError("Password cannot be empty")
        
        ks_manager.add_credential(name, user, password)
        print(f"✓ Credential '{name}' created successfully")
