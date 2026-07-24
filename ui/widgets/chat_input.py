from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
)
from PySide6.QtCore import Qt, Signal
from ui.theme import *


class MessageInput(QTextEdit):
    sendRequested = Signal()

    def keyPressEvent(self, event):
        if (
            event.key() in (Qt.Key_Return, Qt.Key_Enter)
            and not (event.modifiers() & Qt.ShiftModifier)
        ):
            self.sendRequested.emit()
            return

        super().keyPressEvent(event)


class ChatInput(QWidget):

    sendClicked = Signal(str)

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.input = MessageInput()

        self.input.setPlaceholderText("BİLGE'ye mesaj yaz...")
        self.input.setFixedHeight(70)

        self.input.setStyleSheet(f"""
        QTextEdit {{
            background:{CARD};
            color:{TEXT};
            border:1px solid {BORDER};
            border-radius:14px;
            padding:12px;
            font-size:14px;
        }}

        QTextEdit:focus {{
            border:1px solid {ACCENT};
        }}
        """)

        self.voice_btn = QPushButton("🎤")
        self.voice_btn.setFixedSize(50, 50)

        self.voice_btn.setStyleSheet(f"""
        QPushButton {{
            background:{CARD};
            color:{TEXT};
            border:none;
            border-radius:12px;
            font-size:18px;
        }}

        QPushButton:hover {{
            background:{HOVER};
        }}
        """)

        self.send_btn = QPushButton("➤")
        self.send_btn.setFixedSize(50, 50)

        self.send_btn.setStyleSheet(f"""
        QPushButton {{
            background:{ACCENT};
            color:black;
            border:none;
            border-radius:12px;
            font-size:18px;
            font-weight:bold;
        }}

        QPushButton:hover {{
            background:#5EEAD4;
        }}
        """)

        layout.addWidget(self.input, 1)
        layout.addWidget(self.voice_btn)
        layout.addWidget(self.send_btn)

        self.send_btn.clicked.connect(self.emit_message)
        self.input.sendRequested.connect(self.emit_message)

    def emit_message(self):

        text = self.input.toPlainText().strip()

        if not text:
            return

        self.sendClicked.emit(text)

        self.input.clear()