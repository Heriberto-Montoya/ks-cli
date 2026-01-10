from .command_strategy import CommandStrategy
from ks.gui.keystore_app import KeystoreApp
from ks.keystore.keystore_manager import KeyStoreManager

class GuiStrategy(CommandStrategy):
    def __init__(self, ks_manager: KeyStoreManager):
        self.ks_manager = ks_manager

    def execute(self, args):
        gui = KeystoreApp(self.ks_manager)
        gui.run()