from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label, ListView, ListItem

from ks.gui.keylist_app import KeyListApp
from ks.keystore.keystore_manager import KeyStoreManager

class SidebarApp(Vertical):


  def __init__(self, ks_manager: KeyStoreManager):
    super().__init__()
    self.ks_manager = ks_manager
    self.keys_list = KeyListApp(ks_manager)


  def compose(self) -> ComposeResult:
    yield Label("Keys available", classes="section-title")
    yield self.keys_list
      