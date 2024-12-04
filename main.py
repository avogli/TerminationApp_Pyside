# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QListView, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1308, 892)
        MainWindow.setStyleSheet(u"""
/* General Reset */
* {
    margin: 0;
    padding: 0;
    font-family: "Roboto", "Arial", "Helvetica", sans-serif;
}

/* Main Window */
QMainWindow {
    background-color: #f0f2f6; /* Light gray background */
    color: #262730; /* Dark text color */
}

/* QFrame (Main Component) */
QFrame {
    background-color: #f0f2f6; /* White background for content area */
    border-radius: 8px; /* Rounded corners */
    border: 1px solid #d0d4d9; /* Light border */
    padding: 0px;
}

/* QLabel (Headers and Text) */
QLabel {
    color: #1a1b1e;
    font-size: 16px;
    line-height: 1.6;
}

QLabel#header {
    font-size: 24px;
    font-weight: bold;
    color: #1a1b1e;
    margin-bottom: 16px;
}

QLabel#subheader {
    font-size: 20px;
    font-weight: 500;
    color: #6d6f74;
    margin-bottom: 12px;
}

/* QPushButton (Buttons) */
QPushButton {
    background-color: #29ba74;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #108550;
}

QPushButton:pressed {
    background-color: #108550;
}

/* QLineEdit (Text Inputs) */
QLineEdit {
    background-color: #ffffff;
    border: 1px solid #d0d4d9;
    border-radius: 6px;
    padding: 6px 12px;
    color: #262730;
    font-size: 14px;
}

QLineEdit:focus {
    border: 1px solid #1f77b4;
    outline: none;
}

/* QGroupBox (Section Containers) */
QGroupBox {
    background-color: #ffffff;
    border: 1px solid #ffffff; /* Same as the QFrame background */
    border-radius: 8px; /* Rounded corners for visual consistency */
    margin-top: 2px; /* Spacing between group boxes */
    padding: 2px; /* Inner padding for content */
    font-size: 16px; /* Font size for the title */
    font-weight: bold; /* Bold title text */
    color: #262730; /* Dark text for the title */
}

QGroupBox::title {
    subcontrol-origin: margin; /* Title position */
    subcontrol-position: top left; /* Align title to the top-left */
    padding: 0 8px; /* Padding around the title text */
    background-color: #f0f2f6; /* Subtle background for title text */
    color: #1f77b4; /* Streamlit-style blue for title text */
    border-radius: 4px; /* Rounded background for the title */
    font-size: 14px; /* Slightly smaller font for title text */
    font-weight: bold; /* Bold for emphasis */
}

/* QComboBox (Dropdowns) */
QComboBox {
    background-color: #ffffff;
    border: 1px solid #d0d4d9;
    border-radius: 6px;
    padding: 6px 12px;
    color: #262730;
    font-size: 14px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #d0d4d9;
    border-radius: 6px;
}

/* QCheckBox (Checkboxes) */
QCheckBox {
    color: #1a1b1e;
    font-size: 14px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 1px solid #d0d4d9;
    border-radius: 4px;
    background-color: #ffffff;
}

QCheckBox::indicator:checked {
    background-color: #1f77b4;
    border: 1px solid #1f77b4;
}

/* QScrollBar (Scrollbars) */
QScrollBar:vertical {
    border: none;
    background: #f0f2f6;
    width: 12px;
    margin: 16px 0;
}

QScrollBar::handle:vertical {
    background: #d0d4d9;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background: #b0b4b9;
}

QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    height: 0;
    width: 0;
}

/* QProgressBar */
QProgressBar {
    border: 1px solid #d0d4d9;
    border-radius: 8px;
    background: #e6e8eb;
    text-align: center;
    color: #565a5e;
}

QProgressBar::chunk {
    background-color: #1f77b4;
    border-radius: 8px;
}

/* Tooltips */
QToolTip {
    background-color: #1a1b1e;
    color: #ffffff;
    border: 1px solid #d0d4d9;
    padding: 4px;
    border-radius: 4px;
    font-size: 12px;
}

/* QMessageBox */
QMessageBox {
    background-color: #ffffff;
    border: 1px solid #d0d4d9;
    border-radius: 8px;
    padding: 16px;
    font-size: 14px;
    color: #262730;
}

QMessageBox QLabel {
    color: #1a1b1e;
    font-size: 16px;
    font-weight: normal;
    margin-bottom: 8px;
}

QMessageBox QPushButton {
    background-color: #29ba74;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: bold;
}

QMessageBox QPushButton:hover {
    background-color: #108550;
}

QMessageBox QPushButton:pressed {
    background-color: #108550;
}

/* QTableView Headers */
QHeaderView::section {
    background-color: #f0f2f6;
    border: 1px solid #d0d4d9;
    padding: 8px;
    color: #262730;
    font-size: 14px;
    font-weight: bold;
    text-align: left;
}

QHeaderView::section:hover {
    background-color: #e0e2e7;
}

QHeaderView::section:pressed {
    background-color: #d0d4d9;
}

/* QTableView */
QTableView {
    background-color: #ffffff;
    border: 1px solid #d0d4d9;
    gridline-color: #d0d4d9;
    font-size: 14px;
    color: #262730;
}""")



        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1244, 3018))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 3000))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.GB_header = QGroupBox(self.frame)
        self.GB_header.setObjectName(u"GB_header")
        self.horizontalLayout_2 = QHBoxLayout(self.GB_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_4 = QGroupBox(self.GB_header)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Old_report_LBL = QLabel(self.groupBox_2)
        self.Old_report_LBL.setObjectName(u"Old_report_LBL")
        self.Old_report_LBL.setMinimumSize(QSize(200, 40))

        self.verticalLayout_2.addWidget(self.Old_report_LBL)

        self.new_report_LBL = QLabel(self.groupBox_2)
        self.new_report_LBL.setObjectName(u"new_report_LBL")
        self.new_report_LBL.setMinimumSize(QSize(200, 40))

        self.verticalLayout_2.addWidget(self.new_report_LBL)

        self.Trello_LBL = QLabel(self.groupBox_2)
        self.Trello_LBL.setObjectName(u"Trello_LBL")
        self.Trello_LBL.setMinimumSize(QSize(200, 40))

        self.verticalLayout_2.addWidget(self.Trello_LBL)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 40))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 40))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(200, 40))

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.groupBox)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.horizontalSpacer = QSpacerItem(900, 78, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addWidget(self.GB_header)

        self.GB_old_report_preview = QGroupBox(self.frame)
        self.GB_old_report_preview.setObjectName(u"GB_old_report_preview")
        self.horizontalLayout_4 = QHBoxLayout(self.GB_old_report_preview)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.groupBox_6 = QGroupBox(self.GB_old_report_preview)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(818, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.TW_old_report_preview = QTableView(self.groupBox_6)
        self.TW_old_report_preview.setObjectName(u"TW_old_report_preview")

        self.verticalLayout_4.addWidget(self.TW_old_report_preview)


        self.horizontalLayout_4.addWidget(self.groupBox_6)

        self.horizontalSpacer_4 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addWidget(self.GB_old_report_preview)

        self.GB = QGroupBox(self.frame)
        self.GB.setObjectName(u"GB")
        self.horizontalLayout_5 = QHBoxLayout(self.GB)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.groupBox_9 = QGroupBox(self.GB)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(818, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addWidget(self.groupBox_10)

        self.Preview_new_report_TV = QTableView(self.groupBox_9)
        self.Preview_new_report_TV.setObjectName(u"Preview_new_report_TV")

        self.verticalLayout_5.addWidget(self.Preview_new_report_TV)


        self.horizontalLayout_5.addWidget(self.groupBox_9)

        self.horizontalSpacer_7 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addWidget(self.GB)

        self.GB_Trello = QGroupBox(self.frame)
        self.GB_Trello.setObjectName(u"GB_Trello")
        self.horizontalLayout_7 = QHBoxLayout(self.GB_Trello)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.groupBox_12 = QGroupBox(self.GB_Trello)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_13 = QGroupBox(self.groupBox_12)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.groupBox_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.horizontalSpacer_9 = QSpacerItem(818, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addWidget(self.groupBox_13)

        self.Preview_trello_TV = QTableView(self.groupBox_12)
        self.Preview_trello_TV.setObjectName(u"Preview_trello_TV")

        self.verticalLayout_7.addWidget(self.Preview_trello_TV)


        self.horizontalLayout_7.addWidget(self.groupBox_12)

        self.horizontalSpacer_10 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_11.addWidget(self.GB_Trello)

        self.GB_Trello_2 = QGroupBox(self.frame)
        self.GB_Trello_2.setObjectName(u"GB_Trello_2")
        self.horizontalLayout_14 = QHBoxLayout(self.GB_Trello_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_17 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.groupBox_14 = QGroupBox(self.GB_Trello_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_17 = QGroupBox(self.groupBox_14)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.groupBox_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_15.addWidget(self.label_9)

        self.horizontalSpacer_20 = QSpacerItem(818, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)


        self.verticalLayout_10.addWidget(self.groupBox_17)

        self.Differences_LV = QListView(self.groupBox_14)
        self.Differences_LV.setObjectName(u"Differences_LV")

        self.verticalLayout_10.addWidget(self.Differences_LV)


        self.horizontalLayout_14.addWidget(self.groupBox_14)

        self.horizontalSpacer_21 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_21)


        self.verticalLayout_11.addWidget(self.GB_Trello_2)

        self.GB_first_comparison = QGroupBox(self.frame)
        self.GB_first_comparison.setObjectName(u"GB_first_comparison")
        self.horizontalLayout_9 = QHBoxLayout(self.GB_first_comparison)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.groupBox_15 = QGroupBox(self.GB_first_comparison)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_16 = QGroupBox(self.groupBox_15)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.groupBox_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_10.addWidget(self.label_7)

        self.horizontalSpacer_12 = QSpacerItem(818, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addWidget(self.groupBox_16)

        self.Preview_old_new_report_TV = QTableView(self.groupBox_15)
        self.Preview_old_new_report_TV.setObjectName(u"Preview_old_new_report_TV")

        self.verticalLayout_8.addWidget(self.Preview_old_new_report_TV)


        self.horizontalLayout_9.addWidget(self.groupBox_15)

        self.horizontalSpacer_13 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addWidget(self.GB_first_comparison)

        self.GB_Final_results = QGroupBox(self.frame)
        self.GB_Final_results.setObjectName(u"GB_Final_results")
        self.horizontalLayout_11 = QHBoxLayout(self.GB_Final_results)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)

        self.groupBox_18 = QGroupBox(self.GB_Final_results)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_19 = QGroupBox(self.groupBox_18)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(self.groupBox_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(400, 50))

        self.horizontalLayout_12.addWidget(self.label_8)

        self.horizontalSpacer_15 = QSpacerItem(818, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)


        self.verticalLayout_9.addWidget(self.groupBox_19)

        self.Preview_Final_results_TV = QTableView(self.groupBox_18)
        self.Preview_Final_results_TV.setObjectName(u"Preview_Final_results_TV")

        self.verticalLayout_9.addWidget(self.Preview_Final_results_TV)


        self.horizontalLayout_11.addWidget(self.groupBox_18)

        self.horizontalSpacer_16 = QSpacerItem(158, 358, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)


        self.verticalLayout_11.addWidget(self.GB_Final_results)

        self.groupBox_20 = QGroupBox(self.frame)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_18 = QSpacerItem(431, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.Download_BTN = QPushButton(self.groupBox_20)
        self.Download_BTN.setObjectName(u"Download_BTN")
        self.Download_BTN.setMinimumSize(QSize(300, 50))

        self.horizontalLayout_13.addWidget(self.Download_BTN)

        self.horizontalSpacer_19 = QSpacerItem(431, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_19)


        self.verticalLayout_11.addWidget(self.groupBox_20)


        self.verticalLayout_6.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GB_header.setTitle("")
        self.groupBox_4.setTitle("")
        self.groupBox_2.setTitle("")
        self.Old_report_LBL.setText(QCoreApplication.translate("MainWindow", u"Load Old Report", None))
        self.new_report_LBL.setText(QCoreApplication.translate("MainWindow", u"Load New Report", None))
        self.Trello_LBL.setText(QCoreApplication.translate("MainWindow", u"Load Trello", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.GB_old_report_preview.setTitle("")
        self.groupBox_6.setTitle("")
        self.groupBox_5.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Old Report Preview", None))
        self.GB.setTitle("")
        self.groupBox_9.setTitle("")
        self.groupBox_10.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"New Report Preview", None))
        self.GB_Trello.setTitle("")
        self.groupBox_12.setTitle("")
        self.groupBox_13.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Trello Report Preview", None))
        self.GB_Trello_2.setTitle("")
        self.groupBox_14.setTitle("")
        self.groupBox_17.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Changed values in New report", None))
        self.GB_first_comparison.setTitle("")
        self.groupBox_15.setTitle("")
        self.groupBox_16.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Old and New Report comparison", None))
        self.GB_Final_results.setTitle("")
        self.groupBox_18.setTitle("")
        self.groupBox_19.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Final Report Preview", None))
        self.groupBox_20.setTitle("")
        self.Download_BTN.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

