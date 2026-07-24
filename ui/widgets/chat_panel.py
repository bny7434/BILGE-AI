from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QWidget,
    QScrollArea,
)

from PySide6.QtCore import Qt

from ui.theme import *


class MessageBubble(QFrame):

    def __init__(self, text, is_user=False):
        super().__init__()

        layout = QHBoxLayout(self)

        if is_user:
            layout.addStretch()

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setMaximumWidth(650)

        color = ACCENT if is_user else CARD
        text_color = "#000000" if is_user else TEXT

        bubble.setStyleSheet(f"""
        QLabel{{
            background:{color};
            color:{text_color};
            padding:16px;
            border-radius:16px;
            font-size:14px;
        }}
        """)

        layout.addWidget(bubble)

        if not is_user:
            layout.addStretch()


class ChatPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"""
        QFrame{{
            background:{PANEL};
            border-radius:{RADIUS}px;
        }}
        """)

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(15)

        title = QLabel("BİLGE AI")

        title.setStyleSheet(f"""
        QLabel{{
            color:{TEXT};
            font-size:28px;
            font-weight:bold;
        }}
        """)

        layout.addWidget(title)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.NoFrame)

        self.container = QWidget()

        self.messages = QVBoxLayout(self.container)
        self.messages.setAlignment(Qt.AlignTop)
        self.messages.setSpacing(15)

        self.scroll.setWidget(self.container)

        layout.addWidget(self.scroll,1)

        self.input = QTextEdit()

        self.input.setPlaceholderText("BİLGE'ye mesaj yaz...")

        self.input.setFixedHeight(60)

        self.input.setStyleSheet(f"""
        QTextEdit{{
            background:{CARD};
            color:{TEXT};
            border:none;
            border-radius:12px;
            padding:12px;
            font-size:14px;
        }}
        """)

        self.send = QPushButton("Gönder")

        self.send.setFixedHeight(60)

        self.send.setStyleSheet(f"""
        QPushButton{{
            background:{ACCENT};
            color:black;
            border:none;
            border-radius:12px;
            font-weight:bold;
        }}

        QPushButton:hover{{
            background:#5EEAD4;
        }}
        """)

        bottom = QHBoxLayout()

        bottom.addWidget(self.input,1)
        bottom.addWidget(self.send)

        layout.addLayout(bottom)

        self.send.clicked.connect(self.send_message)

        self.add_ai_message("Merhaba 👋\nBen BİLGE.\nHazırım.")

    def add_ai_message(self,text):

        self.messages.addWidget(
            MessageBubble(text)
        )

    def add_user_message(self,text):

        self.messages.addWidget(
            MessageBubble(text,True)
        )

    def send_message(self):

        text=self.input.toPlainText().strip()

        if not text:
            return

        self.add_user_message(text)

        self.input.clear()