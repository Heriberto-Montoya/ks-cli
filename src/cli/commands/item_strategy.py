from abc import ABC, abstractmethod
from ..keystore.keystore_manager import KeyStoreManager

class ItemStrategy(ABC):
    @abstractmethod
    def create(self, ks_manager: KeyStoreManager, name: str, args):
        pass
