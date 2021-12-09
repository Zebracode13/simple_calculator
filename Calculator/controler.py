import sys
from PyQt5.QtWidgets import(QApplication)

from app import PyCalculator
from functools import partial

class CalController():
    def __init__(self, model, view):
        self._view =  view
        self._model = model
        self.signal_connecoter()

    def calculate_result(self):
        rs = self._model(expression=self._view.displayText())
        self._view.setDisplayText(rs)

    def build_expression(self, expes):
        if self._view.displayText() == ZeroDivisionError:
            self._view.clearDisplay()

        expression = self._view.displayText() + expes
        self._view.setDisplayText(expression)


    def signal_connecoter(self):
        for btnTxt, btn in self._view.buttons.items():
            if btnTxt not in {'=', 'C'}:
                btn.clicked.connect(partial(self.build_expression, btnTxt))

        self._view.buttons['='].clicked.connect(self.calculate_result)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


def evaluate_expression(expression):
    try:
        rs = str(eval(expression, {}, {}))
    except Exception:
        rs = "Erro:"
    return rs


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    view = PyCalculator()
    
    view.show()
    model = evaluate_expression

    CalController(model=model, view=view)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()