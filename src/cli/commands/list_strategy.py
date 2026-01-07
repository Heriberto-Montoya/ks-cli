from .command_strategy import CommandStrategy
from keystore.keystore_manager import KeyStoreManager
from tui.tui_list import print_keystore_list

class ListStrategy(CommandStrategy):
  def __init__(self, ks_manager: KeyStoreManager):
    self.ks_manager = ks_manager
  
  def execute(self, args):
    verbose = getattr(args, 'verbose', False)
    password = getattr(args, 'password', False)
    list = self.ks_manager.list()
    print_keystore_list(list, verbose, password)