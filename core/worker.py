from PySide6.QtCore import QObject, Signal, Slot


class AIWorker(QObject):

    finished = Signal(str)

    def __init__(self, manager, prompt):
        super().__init__()

        self.manager = manager
        self.prompt = prompt

    @Slot()
    def run(self):

        answer = self.manager.ask(self.prompt)

        self.finished.emit(answer)