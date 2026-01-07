from .command_strategy import CommandStrategy
from ..keystore.keystore_manager import KeyStoreManager
from ..tui.tui_list import print_keystore_list


class SearchStrategy(CommandStrategy):
    def __init__(self, ks_manager: KeyStoreManager):
        self.ks_manager = ks_manager

    def execute(self, args):
        query = (getattr(args, "query", None) or "").strip()
        type_filter = getattr(args, "type", None)
        verbose = getattr(args, "verbose", False)
        password = getattr(args, "password", False)

        if not query:
            print("You must specify a search query..")
            return

        vault = self.ks_manager.list() or {}

        q = query.lower()
        filtered = {}

        for name, data in vault.items():
            if type_filter and data.get("type_key") != type_filter:
                continue

            # Search in name and in common fields
            found = False
            if q in str(name).lower():
                found = True

            # check user, password, content fields
            for key in ("user", "password", "content"):
                if not found:
                    val = data.get(key)
                    if val is not None and q in str(val).lower():
                        found = True
                        break

            if found:
                filtered[name] = data

        if not filtered:
            print(f"No se encontraron elementos para: '{query}'")
            return

        print_keystore_list(filtered, verbose, password)
