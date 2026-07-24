from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from PySide6.QtCore import Qt

from ui.theme import *


class MenuButton(QPushButton):

    def __init__(self, text):
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(46)

        self.setStyleSheet(f"""
        QPushButton {{
            background: transparent;
            color: {TEXT};
            border: none;
            border-radius: 12px;
            padding-left: 18px;
            text-align: left;
            font-size: 14px;
        }}

        QPushButton:hover {{
            background: {HOVER};
        }}

        QPushButton:pressed {{
            background: {ACCENT};
            color: black;
        }}
        """)


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(260)

        self.setStyleSheet(f"""
        QFrame {{
            background: {PANEL};
            border-radius: {RADIUS}px;
        }}

        QLabel {{
            color: {TEXT};
        }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18,18,18,18)
        layout.setSpacing(12)

        logo = QLabel("🤖 BİLGE")
        logo.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        layout.addWidget(logo)

        layout.addSpacing(20)

        self.new_chat = MenuButton("➕  Yeni Sohbet")
        self.history = MenuButton("💬  Sohbet Geçmişi")
        self.system = MenuButton("📊  Sistem")
        self.settings = MenuButton("⚙️  Ayarlar")

        layout.addWidget(self.new_chat)
        layout.addWidget(self.history)
        layout.addWidget(self.system)
        layout.addWidget(self.settings)

        layout.addStretch()

        version = QLabel("BİLGE v3.0")
        version.setAlignment(Qt.AlignCenter)
        version.setStyleSheet(f"""
            color:{SECONDARY};
            font-size:12px;
        """)

        layout.addWidget(version)