from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from .InputLayout import InputLayout


class MainLayout(QVBoxLayout):
    """main layout for the application which contains the input layout and confirmation button"""

    def __init__(self):
        super().__init__()

        self.button = QPushButton("Click!")
        self.input_layout = InputLayout()

        self.addLayout(self.input_layout)
        self.addWidget(self.button)