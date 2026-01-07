from keystore.keystore_manager import KeyStoreManager
from .command_strategy import CommandStrategy
from .item_strategy_factory import ItemStrategyFactory


class CreateStrategy(CommandStrategy):  
    def __init__(self, ks_manager: KeyStoreManager):
        self.ks_manager = ks_manager
    
    def execute(self, args):
        try:
            # Validar entrada
            name = getattr(args, 'name', None)
            if not name:
                raise ValueError("Name is required")
            
            item_type = getattr(args, 'type', None)
            if not item_type:
                raise ValueError("Type is required")
            
            # Obtener estrategia y ejecutar
            strategy = ItemStrategyFactory.get_strategy(item_type)
            strategy.create(self.ks_manager, name, args)
            
        except ValueError as e:
            print(f"✗ Error: {e}")
            raise
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
            raise
