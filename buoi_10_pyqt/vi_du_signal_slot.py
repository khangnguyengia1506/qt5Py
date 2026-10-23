import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QVBoxLayout
)


class CuaSo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal - Slot")
        self.resize(350, 180)

        self.o_nhap = QLineEdit()
        self.o_nhap.setPlaceholderText("Nhập nội dung...")

        nut_hien_thi = QPushButton("Hiển thị")
        self.nhan_ket_qua = QLabel("Chưa có nội dung")

        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        # Một signal kết nối với hai slot
        nut_hien_thi.clicked.connect(self.hien_thi)
        nut_hien_thi.clicked.connect(self.in_thong_bao)

    def hien_thi(self):
        noi_dung = self.o_nhap.text()
        self.nhan_ket_qua.setText(f"Bạn vừa nhập: {noi_dung}")

    def in_thong_bao(self):
        print("Nút vừa được bấm!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSo()
    cua_so.show()
    sys.exit(app.exec_())