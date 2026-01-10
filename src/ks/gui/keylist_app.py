from textual.app import App
from textual.widgets import ListView, ListItem, Label

from ks.keystore.keystore_manager import KeyStoreManager


class KeyListApp(ListView):
    def __init__(self, ks_manager: KeyStoreManager) -> None:
        super().__init__()
        self.id = "key_list"
        self.ks_manager = ks_manager

    def on_mount(self) -> None:
        self._fill()

    def _fill(self):
        for item_name, _  in self.ks_manager.list().items():
            self.append(ListItem(Label(item_name)))

