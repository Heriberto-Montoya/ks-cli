from keystore.keystore_manager import KeyStoreManager
from .create_strategy import CreateStrategy
from .list_strategy import ListStrategy


class ExecCommand:  
  def __init__(self, args, master_password: str = "default_password"):
    self.args = args
    self.ks_manager = KeyStoreManager(master_password=master_password)
    self.strategies = {
      "create": CreateStrategy(self.ks_manager),
      "list": ListStrategy(self.ks_manager)
    }
  
  def execute(self):
    command = getattr(self.args, 'command', None)
    
    if command not in self.strategies:
      raise ValueError(f"Unknown command: {command}")
    
    strategy = self.strategies[command]
    return strategy.execute(self.args)