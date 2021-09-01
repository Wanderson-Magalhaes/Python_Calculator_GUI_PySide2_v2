################################################################################
##
## STUDY PROJECT BY: WANDERSON M.
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 0.1
##
################################################################################

# IMPORTS
from qt_core import *
from main_ui import Ui_MainWindow
import files_rc

# IMPORT QSS
from styles import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        #
        # MAIN WINDOW PARAMETERS
        # CHANGE "MainWindow" TO "self"
        #

        self.setObjectName("MainWindow")
        self.resize(350, 600)
        self.setMinimumSize(QtCore.QSize(350, 600))
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ICO/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet(style.mainWindow)

        # IMPORT WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # START - GUI FUNCTIONS
        ########################################################################

        ## TITLE BAR BTS
        ########################################################################

        # MINIMIZE
        self.ui.pushButton_minimize.clicked.connect(lambda: self.showMinimized())

        def maximize():
            if not self.isMaximized():
                self.showMaximized()
                self.ui.pushButton_max_rest.setToolTip("Restore")
                self.ui.pushButton_max_rest.setStyleSheet(style.bts_title_bar_restore)
            elif self.isMaximized():
                self.setWindowState(QtCore.Qt.WindowNoState)
                self.ui.pushButton_max_rest.setToolTip("Maximize")
                self.ui.pushButton_max_rest.setStyleSheet(style.bts_title_bar_maximize)

        self.ui.pushButton_max_rest.clicked.connect(lambda: maximize())

        # CLOSE WINDOW
        self.ui.pushButton_close.clicked.connect(lambda: self.close())

        ## BTS NUMBERS FUNCTIONS
        ########################################################################

        # DEF WRITE NUMBER
        def writeNumber(value):
            numbers = self.ui.lineEdit_values.text()
            self.ui.lineEdit_values.setText(numbers + str(value))
            self.clearRepeat()

        # BTS NUMBERS
        self.ui.bt_0.clicked.connect(lambda: writeNumber(0))
        self.ui.bt_1.clicked.connect(lambda: writeNumber(1))
        self.ui.bt_2.clicked.connect(lambda: writeNumber(2))
        self.ui.bt_3.clicked.connect(lambda: writeNumber(3))
        self.ui.bt_4.clicked.connect(lambda: writeNumber(4))
        self.ui.bt_5.clicked.connect(lambda: writeNumber(5))
        self.ui.bt_6.clicked.connect(lambda: writeNumber(6))
        self.ui.bt_7.clicked.connect(lambda: writeNumber(7))
        self.ui.bt_8.clicked.connect(lambda: writeNumber(8))
        self.ui.bt_9.clicked.connect(lambda: writeNumber(9))
        # DOT
        self.ui.bt_dot.clicked.connect(lambda: writeNumber('.'))

        # BT CLEAR
        def clearFields():
            self.ui.label_temp.setText('')
            self.ui.lineEdit_values.setText('')
            self.ui.lineEdit_values.setFocus()

        self.ui.bt_clear.clicked.connect(lambda: clearFields())


        # BACKSPACE
        self.ui.bt_backspace.clicked.connect(lambda: self.clearClick())


        # Bts Operators
        self.ui.bt_div.clicked.connect(lambda: self.setOperations('÷'))
        self.ui.bt_multiply.clicked.connect(lambda: self.setOperations('x'))
        self.ui.bt_minus.clicked.connect(lambda: self.setOperations('-'))
        self.ui.bt_plus.clicked.connect(lambda: self.setOperations('+'))

        # BT EQUAL
        self.ui.bt_equal.clicked.connect(lambda: self.returnValue())

        # BT CREDITS
        globals()['valueTemp'] = ''
        def showCredits():
            self.ui.bt_copy.setEnabled(False)
            globals()['valueTemp'] = self.ui.lineEdit_values.text()
            self.ui.lineEdit_values.setText('')
            QtCore.QTimer.singleShot(100, lambda: self.ui.lineEdit_values.setPlaceholderText("Created"))
            QtCore.QTimer.singleShot(1300, lambda: self.ui.lineEdit_values.setPlaceholderText("by:"))
            QtCore.QTimer.singleShot(2100, lambda: self.ui.lineEdit_values.setPlaceholderText("Wanderson"))
            QtCore.QTimer.singleShot(3500, lambda: self.ui.lineEdit_values.setPlaceholderText("with"))
            QtCore.QTimer.singleShot(4500, lambda: self.ui.lineEdit_values.setPlaceholderText("Python"))
            QtCore.QTimer.singleShot(5500, lambda: self.ui.lineEdit_values.setPlaceholderText("and"))
            QtCore.QTimer.singleShot(6500, lambda: self.ui.lineEdit_values.setPlaceholderText("PySide2"))
            QtCore.QTimer.singleShot(7500, lambda: self.ui.lineEdit_values.setPlaceholderText(":D"))
            QtCore.QTimer.singleShot(8000, lambda: self.ui.lineEdit_values.setPlaceholderText(""))
            QtCore.QTimer.singleShot(8050, lambda: self.ui.lineEdit_values.setText(globals()['valueTemp']))
            QtCore.QTimer.singleShot(8100, lambda: self.ui.bt_copy.setEnabled(True))

        self.ui.bt_copy.clicked.connect(lambda: showCredits())

        ## KEY PRESSED
        ########################################################################
        self.ui.lineEdit_values.keyPressEvent = self.keyPressEvent

        ## WELCOME TEXT ANIMATION
        ########################################################################
        self.ui.lineEdit_values.setFocus()
        self.ui.bt_copy.setEnabled(False)
        QtCore.QTimer.singleShot(200, lambda: self.ui.lineEdit_values.setPlaceholderText("H"))
        QtCore.QTimer.singleShot(600, lambda: self.ui.lineEdit_values.setPlaceholderText("Hi"))
        QtCore.QTimer.singleShot(1000, lambda: self.ui.lineEdit_values.setPlaceholderText("Hi!"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.lineEdit_values.setPlaceholderText("Welcome!"))
        QtCore.QTimer.singleShot(4000, lambda: self.ui.lineEdit_values.setPlaceholderText("..."))
        QtCore.QTimer.singleShot(5000, lambda: self.ui.lineEdit_values.setPlaceholderText("Here we go"))
        QtCore.QTimer.singleShot(6500, lambda: self.ui.lineEdit_values.setPlaceholderText(":D"))
        QtCore.QTimer.singleShot(7800, lambda: self.ui.lineEdit_values.setPlaceholderText(""))
        QtCore.QTimer.singleShot(8000, lambda: self.ui.bt_copy.setEnabled(True))


        ## MOVE WINDOW
        ########################################################################
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                if self.isMaximized():
                    maximize()
                    self.setWindowState(QtCore.Qt.WindowNoState)
                    self.ui.pushButton_max_rest.setStyleSheet(style.bts_title_bar_maximize)

        self.ui.frame_topMenu.mouseMoveEvent = moveWindow
        self.ui.frame_labelTemp.mouseMoveEvent = moveWindow
        #self.label_title.mouseMoveEvent = moveWindow
        self.ui.label_credits.mouseMoveEvent = moveWindow



        ########################################################################
        # END - GUI FUNCTIONS
        ########################################################################

        ## SHOW WINDOW
        self.show()

    ## START -- APP EVENTS
    ############################################################################

    # RESIZE EVENT
    def resizeEvent(self, event):
        self.someFunction()
        return super(Ui, self).resizeEvent(event)

    def someFunction(self):
        if self.height() > 600:
            maximumSize = (self.height() / 20)
            self.ui.frame_lineEdit.setMaximumSize(QSize(16777215, (100 + maximumSize * 2)))
        else:
            self.ui.frame_lineEdit.setMaximumSize(QSize(16777215, 100))

    # MOUSE CLICK
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        self.ui.lineEdit_values.setFocus()

    # BT EQUAL
    def returnValue(self):
        value = self.ui.lineEdit_values.text()
        tempValue = self.ui.label_temp.text()

        if tempValue != '' and value != '':
            join_values = str(tempValue + value).replace(' ', '').replace('÷','/').replace('x','*')
            result = eval(join_values)
            self.ui.label_temp.setText('')
            self.ui.lineEdit_values.setText(str(result))
        self.ui.lineEdit_values.setFocus()


    # JUST NUMBERS AND ".", ","
    def justNumbers(self, value):
        text = str(self.ui.lineEdit_values.text())
        value = str(value)
        clear = ''.join([n for n in value if n.isdigit() or n == '.' or n == ','])
        s = value.isdigit()

        if s:
            self.ui.lineEdit_values.setText(text + value)
            self.clearRepeat()
        else:
            self.ui.lineEdit_values.setText(text + clear)
            self.clearRepeat()
        self.ui.lineEdit_values.setFocus()

    # CLEAR MULTIPLES DOTs
    def clearRepeat(self):
        text = str(self.ui.lineEdit_values.text())
        text = text.replace(',','.').replace('+', '').replace('/', '').replace('*', '').replace('--', '-')
        return self.ui.lineEdit_values.setText(text.replace('..','.'))

    # BT BACKSPACE
    def clearClick(self):
        values = self.ui.lineEdit_values.text()
        if values != '':
            values = values[:-1]
            self.ui.lineEdit_values.setText(values)
        self.ui.lineEdit_values.setFocus()

    # BTS OPERATIONS
    globals()['operator'] = ''
    def setOperations(self, operator):
        value = self.ui.lineEdit_values.text()
        tempValue = self.ui.label_temp.text()

        if tempValue != '' and value != '':
            join_values = str(tempValue + value).replace(' ', '').replace('÷','/').replace('x','*')
            result = eval(join_values)
            self.ui.label_temp.setText(str(result) + ' ' + operator)
            self.ui.lineEdit_values.setText('')
            globals()['operator'] = operator
        elif value != '':
            self.ui.label_temp.setText(value + ' ' + operator)
            self.ui.lineEdit_values.setText('')
            globals()['operator'] = operator
        elif tempValue != '':
            tempValue = tempValue[:-1].replace(' ','')
            self.ui.label_temp.setText(tempValue + ' ' + operator)
            globals()['operator'] = operator
        self.ui.lineEdit_values.setFocus()

    def keyPressEvent(self, event):
        # PRESS ENTER
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.returnValue()
            self.ui.lineEdit_values.setFocus()
            event.accept()

        # BACKSPACE
        if event.key() == Qt.Key_Backspace:
            self.clearClick()

        # OPERATIONS
        if event.text() == '-':
            if self.ui.label_temp.text() == '' and self.ui.lineEdit_values.text() == '':
                self.ui.label_temp.setText('0-')
            self.setOperations('-')
        if event.text() == '+':
            self.setOperations('+')
        if event.text() == '*':
            self.setOperations('x')
        if event.text() == '/':
            self.setOperations('÷')

        # RETURN JUST NUMBERS
        self.justNumbers(event.text())

    ## END -- APP EVENTS
    ############################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/Roboto-Regular.ttf')
    ui = Ui()
    sys.exit(app.exec_())
