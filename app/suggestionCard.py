from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import logging, os, shutil

from template.suggestionCard_ui import Ui_Card

from qt_material import apply_stylesheet

class SuggestionCard(Ui_Card, QFrame):

    def __init__(self, filter :list, path :str, foldername :str='YourFolderName') -> None:
        super(SuggestionCard, self).__init__()

        self.filenames  = filter
        self.path       = path
        self.foldername = foldername

        self.keep_files = True

        #### SETUP ####

        super().setupUi(self)
        # self.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.updateTreeView()
        self.setFolderName(self.foldername)

        #### CONNECTIONS ####
        self.moveBtn.clicked.connect(self.onMoveBtnClicked)
        self.closeBtn.clicked.connect(self.onCloseBtnClicked)
        self.deleteBtn.setEnabled(False) # NOT READY
        
    def updateTreeView(self) -> None:

        self.dirModel = QFileSystemModel()
        self.idx = self.dirModel.setRootPath(self.path)
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.dirModel.setNameFilters(self.filenames)
        # Set setNameFilterDisables to False to hide the non-matching items
        self.dirModel.setNameFilterDisables(False)

        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(self.path))
        
        # Resize the first column in the tree view
        self.treeView.header().resizeSection(0, 200)
        # height = 21
        # self.treeView.setMinimumHeight(int(height * len(self.filenames)) + 25) # 25 is header size
        self.treeView.setMinimumHeight(200)

        # TODO: In case, filename error or not support ex. special characters

    def setFolderName(self, foldername :str) -> None:
        self.foldername = foldername
        self.folderName.setText(self.foldername)

    def onMoveBtnClicked(self):
        # Create the destination folder if it doesn't exist
        destination_folder = os.path.join(self.path, self.folderName.text())
        if not os.path.exists(destination_folder): os.makedirs(destination_folder)

        for filename in self.filenames:
            source_path = os.path.join(self.path, filename); logging.debug(source_path)
            destination_path = os.path.join(destination_folder, filename); logging.debug(destination_path)

            try:
                if self.keep_files:
                    # Copy the file to the destination folder
                    shutil.copy2(source_path, destination_path)
                    logging.info('Copied {} files to folder \'{}\'.'.format(len(self.filenames), self.path))
                else:
                    # Move the file to the destination folder
                    shutil.move(source_path, destination_path)
                    logging.info('Moved {} files to folder \'{}\'.'.format(len(self.filenames), self.path))
            except:
                logging.error("Cannot copy / move file to the destination.")

    def onCloseBtnClicked(self):
        # Hide the suggestion card
        self.hide()
        
        # Remove the suggestion card from its parent layout
        parent_layout = self.parent().layout()
        if parent_layout is not None:
            parent_layout.removeWidget(self)
            self.setParent(None)


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s - %(levelname)s - %(funcName)s]\n%(message)s\n')
    
    # create the application and the main window
    app = QApplication([])
    card = SuggestionCard(
        filter=[
            '1.txt'
            # 'ไฟหงาย+ผ้าขาวข้าง.BMP',
            # '[CourseClub.NET] Udacity - Deep Reinforcement Learning Nanodegree v1.0.0-20220728T040500Z-001.zip', 
            # '[CourseClub.NET] Udacity - Deep Reinforcement Learning Nanodegree v1.0.0-20220728T040500Z-002.zip',
            # '~$FO-TO-07 ใบสำคัญรับเงิน_New(1).xlsx', 
            # '~$FO-TO-07 ใบสำคัญรับเงิน_New.xlsx'
        ],
        path=os.path.join(os.path.expanduser('~'), 'Downloads')
    )

    # setup stylesheet
    apply_stylesheet(app, theme='app/theme/light.xml')
    card.resize(600, 300)

    # run
    card.show()
    app.exec()
    