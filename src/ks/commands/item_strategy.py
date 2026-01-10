from abc import ABC, abstractmethod
from ks.keystore.keystore_manager import KeyStoreManager

class ItemStrategy(ABC):
    @abstractmethod
    def create(self, ks_manager: KeyStoreManager, name: str, args):
        pass
