import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QHBoxLayout
)


class CuaSo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bài 1.2 - Layout")
        self.resize(350, 180)

        layout = QGridLayout()

        layout.addWidget(QLabel("Họ tên:"), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)

        layout.addWidget(QLabel("Tuổi:"), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)

        hang_nut = QHBoxLayout()
        hang_nut.addWidget(QPushButton("Đồng ý"))
        hang_nut.addWidget(QPushButton("Hủy"))

        layout.addLayout(hang_nut, 2, 0, 1, 2)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSo()
    cua_so.show()
    sys.exit(app.exec_())