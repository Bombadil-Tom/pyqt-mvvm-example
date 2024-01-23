import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class CounterView(QWidget):
    def __init__(self, viewModel):
        super().__init__()
        self._viewModel = viewModel  # The ViewModel instance
        self._viewModel.countChanged.connect(self.updateLabel)  # Connect signal to the slot
        self.initUI()  # Initialize the UI

    def initUI(self):
        self.setWindowTitle('Counter')  # Window title
        self.layout = QVBoxLayout()  # Vertical layout
        self.label = QLabel('0')  # Label to show the count
        self.layout.addWidget(self.label)
        self.button = QPushButton('Increment')  # Button to increment the count
        self.button.clicked.connect(self._viewModel.increment)  # Connect button click to ViewModel
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)  # Set the layout of the widget

    def updateLabel(self, count):
        self.label.setText(str(count))  # Update the label with the current count