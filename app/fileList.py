import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QFileInfo

class FileDetailsViewer(QMainWindow):
    def __init__(self, file_paths):
        super(FileDetailsViewer, self).__init__()

        self.setWindowTitle("File Details Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.file_paths = file_paths

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["File Name", "Modified Date", "Size"])
        # self.table_widget.horizontalHeader().setSectionResizeMode(0, QTableWidget.Stretch)
        # self.table_widget.horizontalHeader().setSectionResizeMode(1, QTableWidget.ResizeToContents)
        # self.table_widget.horizontalHeader().setSectionResizeMode(2, QTableWidget.ResizeToContents)

        self.populate_table()

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.table_widget)

    def populate_table(self):
        for file_path in self.file_paths:
            file_info = QFileInfo(file_path)
            file_name = file_info.fileName()
            modified_date = file_info.lastModified().toString(Qt.DefaultLocaleLongDate)
            size = file_info.size()

            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            self.table_widget.setItem(row_position, 0, QTableWidgetItem(file_name))
            self.table_widget.setItem(row_position, 1, QTableWidgetItem(modified_date))
            self.table_widget.setItem(row_position, 2, QTableWidgetItem(f"{size} bytes"))

def main():
    app = QApplication(sys.argv)

    file_paths = [
        r'C:\Users\uSeR\Downloads\medicine-ruler.pdf', 
        r'C:\Users\uSeR\Downloads\rules_mm.pdf', 
    ]  # Replace with your file paths
    viewer = FileDetailsViewer(file_paths)
    viewer.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
