import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 连接信号和槽
        self.ui.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.ui.label.setText("Hello, PySide6!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())