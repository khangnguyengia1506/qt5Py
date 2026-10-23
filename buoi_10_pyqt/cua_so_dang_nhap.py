import sys
from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        duong_dan_ui = Path(__file__).resolve().parent / "form_dang_nhap.ui"
        uic.loadUi(str(duong_dan_ui), self)

        self.setWindowTitle("Đăng nhập")
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text().strip()
        mat_khau = self.o_nhap_mat_khau.text()

        if not tai_khoan or not mat_khau.strip():
            QMessageBox.warning(
                self,
                "Thiếu thông tin",
                "Vui lòng nhập đầy đủ tài khoản và mật khẩu."
            )
            return

        QMessageBox.information(
            self,
            "Thông báo",
            f"Xin chào {tai_khoan}! Bạn đã nhập đủ thông tin."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())