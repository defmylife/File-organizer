# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suggestionCard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Card(object):
    def setupUi(self, Card):
        if not Card.objectName():
            Card.setObjectName(u"Card")
        Card.resize(320, 240)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Card.sizePolicy().hasHeightForWidth())
        Card.setSizePolicy(sizePolicy)
        Card.setAutoFillBackground(False)
        Card.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Card)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mode = QLabel(Card)
        self.mode.setObjectName(u"mode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mode.sizePolicy().hasHeightForWidth())
        self.mode.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.mode)

        self.folderName = QLineEdit(Card)
        self.folderName.setObjectName(u"folderName")

        self.horizontalLayout_2.addWidget(self.folderName)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.closeBtn = QPushButton(Card)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy2)
        self.closeBtn.setFlat(True)

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.treeView = QTreeView(Card)
        self.treeView.setObjectName(u"treeView")
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.treeView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.deleteBtn = QPushButton(Card)
        self.deleteBtn.setObjectName(u"deleteBtn")

        self.horizontalLayout.addWidget(self.deleteBtn)

        self.moveBtn = QPushButton(Card)
        self.moveBtn.setObjectName(u"moveBtn")

        self.horizontalLayout.addWidget(self.moveBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Card)

        QMetaObject.connectSlotsByName(Card)
    # setupUi

    def retranslateUi(self, Card):
        Card.setWindowTitle(QCoreApplication.translate("Card", u"Card", None))
        self.mode.setText(QCoreApplication.translate("Card", u"(Add)", None))
        self.folderName.setText(QCoreApplication.translate("Card", u"Folder01", None))
        self.closeBtn.setText(QCoreApplication.translate("Card", u"close", None))
        self.deleteBtn.setText(QCoreApplication.translate("Card", u"Delete", None))
        self.moveBtn.setText(QCoreApplication.translate("Card", u"Move", None))
    # retranslateUi

