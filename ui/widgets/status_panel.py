from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout

from ui.theme import *


class StatusPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(320)

        self.setStyleSheet(f"""
        QFrame{{
            background:{PANEL};
            border-radius:{RADIUS}px;
        }}

        QLabel{{
            color:{TEXT};
            font-size:18px;
            font-weight:bold;
        }}
        """)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Sistem"))

        layout.addStretch()