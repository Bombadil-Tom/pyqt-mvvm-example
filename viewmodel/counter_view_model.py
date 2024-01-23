from PyQt6.QtCore import QObject, pyqtSignal

class CounterViewModel(QObject):
    countChanged = pyqtSignal(int)  # Signal to update the count in the view

    def __init__(self, model):
        super().__init__()
        self._model = model  # Reference to the model
    def increment(self):
        self._model.increment()  # Call increment of the model
        self.countChanged.emit(self._model.count)  # Emit the updated count