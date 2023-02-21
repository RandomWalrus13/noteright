from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)


class NoteRightWindow(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("fusion")
    window = NoteRightWindow()
    window.show()
    app.exec()
