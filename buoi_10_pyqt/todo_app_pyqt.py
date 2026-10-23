import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QListWidget, QVBoxLayout,
    QHBoxLayout, QMessageBox
)


class UngDungToDo(QWidget):
    def __init__(self):
        super().__init__()
        self.danh_sach_cong_viec = []
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.setWindowTitle("Ghi chú công việc - PyQt")
        self.resize(480, 400)

        tieu_de = QLabel("TO-DO LIST")
        tieu_de.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.o_nhap = QLineEdit()
        self.o_nhap.setPlaceholderText("Nhập công việc mới...")

        nut_them = QPushButton("Thêm")
        nut_them.clicked.connect(self.them_cong_viec)
        self.o_nhap.returnPressed.connect(self.them_cong_viec)

        hang_nhap = QHBoxLayout()
        hang_nhap.addWidget(self.o_nhap)
        hang_nhap.addWidget(nut_them)

        self.danh_sach_hien_thi = QListWidget()

        nut_hoan_thanh = QPushButton("Đánh dấu hoàn thành")
        nut_hoan_thanh.clicked.connect(self.danh_dau_hoan_thanh)

        nut_xoa = QPushButton("Xóa công việc")
        nut_xoa.clicked.connect(self.xoa_cong_viec)

        hang_nut = QHBoxLayout()
        hang_nut.addWidget(nut_hoan_thanh)
        hang_nut.addWidget(nut_xoa)

        layout = QVBoxLayout()
        layout.addWidget(tieu_de)
        layout.addLayout(hang_nhap)
        layout.addWidget(self.danh_sach_hien_thi)
        layout.addLayout(hang_nut)
        self.setLayout(layout)

    def lam_moi_danh_sach(self, vi_tri=-1):
        self.danh_sach_hien_thi.clear()

        for noi_dung, da_hoan_thanh in self.danh_sach_cong_viec:
            trang_thai = "[Đã xong]" if da_hoan_thanh else "[Chưa xong]"
            self.danh_sach_hien_thi.addItem(
                f"{trang_thai} {noi_dung}"
            )

        if 0 <= vi_tri < len(self.danh_sach_cong_viec):
            self.danh_sach_hien_thi.setCurrentRow(vi_tri)

    def them_cong_viec(self):
        noi_dung = self.o_nhap.text().strip()

        if not noi_dung:
            QMessageBox.warning(
                self, "Thông báo", "Vui lòng nhập công việc."
            )
            return

        self.danh_sach_cong_viec.append((noi_dung, False))
        self.o_nhap.clear()
        self.lam_moi_danh_sach(
            len(self.danh_sach_cong_viec) - 1
        )
        self.o_nhap.setFocus()

    def xoa_cong_viec(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()

        if vi_tri < 0:
            QMessageBox.warning(
                self, "Thông báo", "Vui lòng chọn công việc cần xóa."
            )
            return

        self.danh_sach_cong_viec.pop(vi_tri)
        vi_tri_moi = min(
            vi_tri, len(self.danh_sach_cong_viec) - 1
        )
        self.lam_moi_danh_sach(vi_tri_moi)

    def danh_dau_hoan_thanh(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()

        if vi_tri < 0:
            QMessageBox.warning(
                self, "Thông báo", "Vui lòng chọn một công việc."
            )
            return

        noi_dung, _ = self.danh_sach_cong_viec[vi_tri]
        self.danh_sach_cong_viec[vi_tri] = (noi_dung, True)
        self.lam_moi_danh_sach(vi_tri)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = UngDungToDo()
    cua_so.show()
    sys.exit(app.exec_())