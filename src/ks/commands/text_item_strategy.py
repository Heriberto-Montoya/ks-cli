from ks.keystore.keystore_manager import KeyStoreManager
from .item_strategy import ItemStrategy

class TextItemStrategy(ItemStrategy):
    def create(self, ks_manager: KeyStoreManager, name: str, args):
        value = getattr(args, 'value', '')
        ks_manager.add_note(name, value)
        print(f"✓ Note '{name}' created successfully")
