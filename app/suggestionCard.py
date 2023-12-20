from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import logging, os

from template.suggestionCard_ui import Ui_Card

from qt_material import apply_stylesheet

class SuggestionCard(Ui_Card, QFrame):
    def __init__(self, filter :list, path :str) -> None:
        super(SuggestionCard, self).__init__()

        self.filenames = filter
        self.path = path

        #### SETUP ####

        super().setupUi(self)
        # self.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.updateTreeView()

        #### CONNECTIONS ####
        ...
        
    def updateTreeView(self) -> None:

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(self.path)
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.dirModel.setNameFilters(self.filenames)
        # Set setNameFilterDisables to False to hide the non-matching items
        self.dirModel.setNameFilterDisables(False)

        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(self.path))
        
        self.resize(400, 400)
        # Resize the first column in the tree view
        self.treeView.header().resizeSection(0, 200)


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s - %(levelname)s - %(funcName)s]\n%(message)s\n')
    
    # create the application and the main window
    app = QApplication([])
    card = SuggestionCard(
        filter=[
            '(Exp) Application form 2023.xlsx', 
            '(Knowledge Science) Application Guide for MEXT Oct 2024.pdf', 
            '2003.05155.pdf', 
            '2022-11-28 14-47-25.mp4', 
            '2023-08-25_10-50-14.mkv', 
            '2023-09-15 09-46-23 (1).mp4', 
            '2023-09-15 09-46-23.mp4', 
            '2023-10-27 16-02-22 - frame at 0m21s.jpg', 
            '2023-10-27 16-02-22 - frame at 0m52s.jpg', 
            '2023-10-27 16-02-22.mp4'
        ],
        path=os.path.join(os.path.expanduser('~'), 'Downloads')
    )

    # setup stylesheet
    # apply_stylesheet(app, theme='light_amber.xml')

    # run
    card.show()
    app.exec()
    