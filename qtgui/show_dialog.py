#
# Show a qt message dialog
#

from PyQt5.QtWidgets import QDialog
from qtgui.gen import (messageGenerated,
                 confirmGenerated,
                 lineEditEntryGenerated,
                 numpadGenerated)


def show_message_dialog(text):
    """
        Shows a generic message dialog to the user displaying the text
        passed. Utilizes word wrap.
    """

    dialog = QDialog()
    interface = messageGenerated.Ui_Dialog()
    interface.setupUi(dialog)
    interface.label.setText(text)
    dialog.exec_()


def show_confirm_dialog(text):
    """
        Shows a generic confirm dialog to the user displaying the text
        passed. Utilizes word wrap.
    """
    dialog = QDialog()
    interface = confirmGenerated.Ui_Dialog()
    interface.setupUi(dialog)
    interface.label.setText(text)
    if dialog.exec_() == 1:
        return True
    return False


def show_line_edit_dialog(text):
     """
         Shows a generic line edit dialog to the user displaying the text
         passed. Utilizes word wrap.
     """
     dialog = QDialog()
     interface = lineEditEntryGenerated.Ui_Dialog()
     interface.setupUi(dialog)
     interface.label.setText(text)
     if dialog.exec_() == 1:
         return True, str(interface.lineEdit.text())
     else:
         return False, ""


class NumpadDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.ui = numpadGenerated.Ui_Dialog()
        self.ui.setupUi(self)
        self.init_signals()
        self.digits = 0
        self.pressed_c()
        self.confirmed = False

    def init_signals(self):
        self.ui.pushButton_1.clicked.connect(self.pressed_1)
        self.ui.pushButton_2.clicked.connect(self.pressed_2)
        self.ui.pushButton_3.clicked.connect(self.pressed_3)
        self.ui.pushButton_4.clicked.connect(self.pressed_4)
        self.ui.pushButton_5.clicked.connect(self.pressed_5)
        self.ui.pushButton_6.clicked.connect(self.pressed_6)
        self.ui.pushButton_7.clicked.connect(self.pressed_7)
        self.ui.pushButton_8.clicked.connect(self.pressed_8)
        self.ui.pushButton_9.clicked.connect(self.pressed_9)
        self.ui.pushButton_0.clicked.connect(self.pressed_0)
        self.ui.pushButton_00.clicked.connect(self.pressed_00)
        self.ui.pushButton_c.clicked.connect(self.pressed_c)
        self.ui.pushButton_confirm.clicked.connect(self.pressed_confirm)

    def pressed_1(self):
        self.append_digits(1)

    def pressed_2(self):
        self.append_digits(2)

    def pressed_2(self):
        self.append_digits(2)

    def pressed_3(self):
        self.append_digits(3)

    def pressed_4(self):
        self.append_digits(4)

    def pressed_5(self):
        self.append_digits(5)

    def pressed_6(self):
        self.append_digits(6)

    def pressed_7(self):
        self.append_digits(7)

    def pressed_8(self):
        self.append_digits(8)

    def pressed_9(self):
        self.append_digits(9)

    def pressed_0(self):
        self.append_digits(0)

    def pressed_00(self):
        self.append_digits(0)
        self.append_digits(0)

    def pressed_c(self):
        self.digits = 0
        self.ui.lineEdit.setText("0.00")

    def pressed_confirm(self):
        self.confirmed = True
        self.close()

    def append_digits(self, v):
        if len(str(self.digits)) == 6:
            return
        self.digits = int(str(self.digits) + str(v))
        digits_string = str(self.digits)
        if len(digits_string) == 1:
            digits_string = "0.0" + digits_string
        elif len(digits_string) == 2:
            digits_string = "0." + digits_string
        else:
            digits_string = digits_string[:-2] + "." + digits_string[len(digits_string)-2:]
        self.ui.lineEdit.setText(digits_string)

if __name__ == "__main__":
    print("No module test implemented.")
