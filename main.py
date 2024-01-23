import sys
from PyQt6.QtWidgets import QApplication
from model.counter_model import CounterModel
from view.counter_view import CounterView
from viewmodel.counter_view_model import CounterViewModel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = CounterModel()
    viewModel = CounterViewModel(model)
    view = CounterView(viewModel)
    view.show()
    sys.exit(app.exec())