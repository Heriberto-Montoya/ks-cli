from .item_strategy import ItemStrategy
from .text_item_strategy import TextItemStrategy
from .credential_item_strategy import CredentialItemStrategy

class ItemStrategyFactory:
    _strategies = {
        "text": TextItemStrategy(),
        "credential": CredentialItemStrategy()
    }
    
    @classmethod
    def get_strategy(cls, item_type: str) -> ItemStrategy:
        """Obtener la estrategia para un tipo de item."""
        if item_type not in cls._strategies:
            raise ValueError(f"Unknown item type: {item_type}. Available: {list(cls._strategies.keys())}")
        return cls._strategies[item_type]