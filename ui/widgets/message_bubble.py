from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

from ui.theme import ACCENT, CARD, TEXT


class MessageBubble(QFrame):
    def __init__(self, text: str, is_user: bool = False):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setTextInteractionFlags(Qt.TextSelectableByMouse)
        bubble.setMaximumWidth(650)

        if is_user:
            background = ACCENT
            foreground = "#000000"
        else:
            background = CARD
            foreground = TEXT

        bubble.setStyleSheet(f"""
        QLabel {{
            background-color: {background};
            color: {foreground};
            border-radius: 16px;
            padding: 14px;
            font-size: 14px;
        }}
        """)

        if is_user:
            layout.addStretch()
            layout.addWidget(bubble)
        else:
            layout.addWidget(bubble)
            layout.addStretch()