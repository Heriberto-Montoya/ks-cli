from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label, ListView, ListItem
from ..keystore.keystore_manager import KeyStoreManager

class SidebarApp(Vertical):
  def __init__(self, ks_manager: KeyStoreManager):
    super().__init__()
    self.ks_manager = ks_manager

  def _create_list(self) -> ListView:
    vault = self.ks_manager.list() or {}
    items = [ListItem(Label(item_name)) for item_name, _ in vault.items()]
    return ListView(*items)

  def compose(self) -> ComposeResult:
    yield Label("Keys avalibles", classes="section-title")
    yield self._create_list()
      