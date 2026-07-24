from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
)

from ui.theme import *
from ui.widgets.sidebar import Sidebar
from ui.widgets.chat_panel import ChatPanel
from ui.widgets.status_panel import StatusPanel


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_window()

        self.build_ui()

    def setup_window(self):

        self.setWindowTitle("BİLGE AI")

        self.resize(1700, 950)

        self.setMinimumSize(1400, 800)

        self.setStyleSheet(f"""
        QWidget{{
            background:{BACKGROUND};
            color:{TEXT};
        }}
        """)

    def build_ui(self):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(20,20,20,20)

        layout.setSpacing(20)

        self.sidebar = Sidebar()

        self.chat = ChatPanel()

        self.status = StatusPanel()

        layout.addWidget(self.sidebar)

        layout.addWidget(self.chat,1)

        layout.addWidget(self.status)