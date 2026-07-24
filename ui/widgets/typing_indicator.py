from PySide6.QtWidgets import QLabel
from ui.theme import TEXT, SECONDARY


class TypingIndicator(QLabel):
    def __init__(self):
        super().__init__("🤖 BİLGE yazıyor...")

        self.setStyleSheet(f"""
        QLabel {{
            color: {SECONDARY};
            font-size: 13px;
            padding: 6px;
        }}
        """)

        self.hide()

    def start(self):
        self.show()

    def stop(self):
        self.hide()