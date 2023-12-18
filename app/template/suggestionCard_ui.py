# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suggestionCard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Card(object):
    def setupUi(self, Card):
        if not Card.objectName():
            Card.setObjectName(u"Card")
        Card.resize(320, 240)
        self.verticalLayout = QVBoxLayout(Card)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.folderName = QLabel(Card)
        self.folderName.setObjectName(u"folderName")

        self.horizontalLayout_2.addWidget(self.folderName)

        self.pushButton_3 = QPushButton(Card)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.treeWidget = QTreeWidget(Card)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(Card)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Card)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Card)

        QMetaObject.connectSlotsByName(Card)
    # setupUi

    def retranslateUi(self, Card):
        Card.setWindowTitle(QCoreApplication.translate("Card", u"Card", None))
        self.folderName.setText(QCoreApplication.translate("Card", u"Folder01", None))
        self.pushButton_3.setText(QCoreApplication.translate("Card", u"close", None))
        self.pushButton_2.setText(QCoreApplication.translate("Card", u"remove", None))
        self.pushButton.setText(QCoreApplication.translate("Card", u"move", None))
    # retranslateUi

