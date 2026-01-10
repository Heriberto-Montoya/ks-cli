from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Label, Input, Button, ListView
from .css import CSS
from ks.keystore.keystore_manager import KeyStoreManager
from .sidebar_app import SidebarApp

class KeystoreApp(App):
    CSS = CSS
    TITLE = "SafeKey TUI"
    BINDINGS = [
        ("q", "quit", "Salir"),
        ("n", "new_key", "Nueva Llave"),
    ]



    def __init__(self, ks_manager: KeyStoreManager):
        super().__init__()
        self.ks_manager = ks_manager
        self.theme = "dracula"
        self.sidebar_app = SidebarApp(self.ks_manager)

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal():
            yield self.sidebar_app


            # with Vertical(id="content-area"):
            #     yield Label("Detalles de la Entrada", classes="section-title")
            #
            #     yield Label("Nombre de la Llave:", classes="field-label")
            #     yield Input(placeholder="Ej: MI_SERVICIO_API", id="input-key")
            #
            #     yield Label("Valor / Contraseña:", classes="field-label")
            #     yield Input(
            #         placeholder="Introduce el valor...", password=True, id="input-value"
            #     )
            #
            #     yield Label("Notas:", classes="field-label")
            #     yield Input(
            #         placeholder="Opcional: ¿Para qué sirve esta llave?",
            #         id="input-notes",
            #     )
            #
            #     with Horizontal(id="buttons-container"):
            #         yield Button("Cancelar", variant="error")
            #         yield Button("Guardar Cambios", variant="success")

        yield Footer()

    def on_mount(self) -> None:
        self.title = "Keystore Manager v1.0"
