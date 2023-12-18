from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
import logging

from template.app_ui import Ui_MainWindow

from qt_material import apply_stylesheet

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        #### SETUP ####

        super().setupUi(self)
        # self.app = Ui_MainWindow()
        # self.app.setupUi(self)

        #### CONNECTIONS ####

        self.selectFolder.clicked.connect(self.handleSelectFolder)
        self.openFolder.clicked.connect(self.handleOpenFolder)

    @Slot()
    def handleSelectFolder(self): 
        ...
        logging.info("Select the folder:")

    @Slot()
    def handleOpenFolder(self): 
        ...
        logging.info("Open the folder:")

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s - %(levelname)s - %(funcName)s]\n%(message)s\n')
    
    # create the application and the main window
    app = QApplication([])
    window = MainWindow()

    # setup stylesheet
    apply_stylesheet(app, theme='light_amber.xml')

    # run
    window.show()
    app.exec()
    