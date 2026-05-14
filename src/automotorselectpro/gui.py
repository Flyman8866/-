from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QTabWidget, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoMotorSelectPro")
        tabs = QTabWidget()
        for name in ["项目概览页", "轴管理页", "计算结果页", "电机推荐页", "BOM 页", "数据库管理页"]:
            page = QWidget()
            layout = QVBoxLayout(page)
            layout.addWidget(QLabel(name))
            tabs.addTab(page, name)
        self.setCentralWidget(tabs)


def run_gui() -> int:
    app = QApplication.instance() or QApplication([])
    w = MainWindow()
    w.resize(900, 600)
    w.show()
    return app.exec()
