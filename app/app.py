from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import logging

from template.app_ui import Ui_MainWindow
from util.dbscan import *
from suggestionCard import *

from qt_material import apply_stylesheet

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # self.suggestionCards = []

        #### SETUP ####

        super().setupUi(self)
        # self.app = Ui_MainWindow()
        # self.app.setupUi(self)
        
        # self.header.setStyleSheet("QWidget {background-color: #FFF}")

        #### CONNECTIONS ####

        self.selectFolder.clicked.connect(self.handleSelectFolder)
        self.openFolder.clicked.connect(self.handleOpenFolder)

    def handleSelectFolder(self): 
        ...
        logging.info("Select the folder:")

        file_paths, _ = getFiles(os.path.join(os.path.expanduser('~'), 'Downloads')) # Fix later

        if file_paths:
            clusters, outlier = dbscan(file_paths)

            # Sort by length of the list
            clusters = dict(sorted(clusters.items(), key=lambda item: len(item[1]), reverse=True))

            c = 0 # For Debug
            
            logging.info("Found {} clusters".format(len(clusters)))
            for i, files_in_cluster in clusters.items():
                
                if i != -1: # Except Outlier
                    
                    card = SuggestionCard(
                        filter=files_in_cluster,
                        path=os.path.join(os.path.expanduser('~'), 'Downloads') # Fix later
                    )
                    self.suggestionSlot.addWidget(card)

                    logging.info("Cluster {} ({}): {}".format(i, len(files_in_cluster), files_in_cluster))
                
                if c >= 3: break # For Debug
                c += 1; print(c)


    def handleOpenFolder(self): 
        ...
        logging.info("Open the folder:")

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s - %(levelname)s - %(funcName)s]\n%(message)s\n')
    
    # create the application and the main window
    app = QApplication([])
    window = MainWindow()

    # setup stylesheet
    # apply_stylesheet(app, theme='light_amber.xml')

    # run
    window.show()
    app.exec()
    