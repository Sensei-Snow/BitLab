#------------------------------------------------------Imports
import sys

#from bitconvertor import *
from conversion import *
import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt, QTimer

#------------------------------------------------------BitLab Window Class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #------------------------------------------------------Set Style
        uic.loadUi("bitlab.ui", self)

        QApplication.setStyle("Windows") # Fusion or WindowsVista

        self.setWindowTitle("Bitlab")

        icon_path = "assets/bitlab.png"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"[ERROR] -- File : {icon_path} not found.")

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        #------------------------------------------------------Adjust UI
        self.input_mode.addItems([
            "<Choose option>",
            "String",
            "Decimal",
            "Binary",
            "Hexadecimal"
        ])

        self.output_mode.addItems([
            "<Choose option>",
            "String",
            "Decimal",
            "Binary",
            "Hexadecimal"
        ])

        #------------------------------------------------------Events
        self.input_mode.currentTextChanged.connect(self.update_combobox_output)
        self.input_mode.currentTextChanged.connect(self.text_changed)
        self.output_mode.currentTextChanged.connect(self.update_combobox_input)
        self.output_mode.currentTextChanged.connect(self.text_changed)

        self.paste_button.clicked.connect(self.paste_clipboard)
        self.copy_button.clicked.connect(self.copy_clipboard)

        self.input_text.textChanged.connect(self.text_changed)

    #------------------------------------------------------Functions
    def update_combobox_output(self):
        input_value = self.input_mode.currentText()
        current_output = self.output_mode.currentText()

        options = ["String", "Decimal", "Binary", "Hexadecimal"]

        self.output_mode.blockSignals(True)

        new_options = ["<Choose option>"] + [o for o in options if o != input_value]

        self.output_mode.clear()
        self.output_mode.addItems(new_options)

        if current_output in new_options:
            self.output_mode.setCurrentText(current_output)

        self.output_mode.blockSignals(False)

    def update_combobox_input(self):
        output_value = self.output_mode.currentText()
        current_input = self.input_mode.currentText()

        options = ["String", "Decimal", "Binary", "Hexadecimal"]

        self.input_mode.blockSignals(True)

        new_options = ["<Choose option>"] + [o for o in options if o != output_value]

        self.input_mode.clear()
        self.input_mode.addItems(new_options)

        if current_input in new_options:
            self.input_mode.setCurrentText(current_input)

        self.input_mode.blockSignals(False)

    def paste_clipboard(self):
        self.input_text.paste()

    def copy_clipboard(self):
        text = self.output_text.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def verify_decimal(integer):
        str_value = str(integer)
        if all(char in "0123456789" + ' ' for char in str_value) and str_value != '':
            return True

    def verify_binary(string):
        if all(char in "01b" + ' ' for char in string) and string != '':
            return True

    def verify_hexadecimal(string):
        if all(char in "0123456789abcdefABCDEFx" + ' ' for char in string) and string != '':
            return True

    def verify_string(string):
        if string != '':
            return True

    def text_changed(self):
        input_value = self.input_mode.currentText()
        output_value = self.output_mode.currentText()
        
        input_text = self.input_text.toPlainText()
        output_text = self.output_text.toPlainText()

        if input_value == "String" and output_value == "Decimal":
            if input_text != "":
                self.output_text.setPlainText(string_to_decimal(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "String" and output_value == "Binary":
            if input_text != "":
                self.output_text.setPlainText(string_to_binary(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "String" and output_value == "Hexadecimal":
            if input_text != "":
                self.output_text.setPlainText(string_to_hexadecimal(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Binary" and output_value == "String":
            if input_text != "":
                self.output_text.setPlainText(binary_to_string(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Binary" and output_value == "Decimal":
            if input_text != "":
                self.output_text.setPlainText(str(binary_to_decimal(input_text)))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Binary" and output_value == "Hexadecimal":
            if input_text != "":
                self.output_text.setPlainText(binary_to_hexadecimal(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Decimal" and output_value == "String":
            if input_text != "":
                self.output_text.setPlainText(decimal_to_string(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Decimal" and output_value == "Binary":
            if input_text != "":
                self.output_text.setPlainText(decimal_to_binary(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Decimal" and output_value == "Hexadecimal":
            if input_text != "":
                self.output_text.setPlainText(decimal_to_hexadecimal(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Hexadecimal" and output_value == "String":
            if input_text != "":
                self.output_text.setPlainText(hexadecimal_to_string(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Hexadecimal" and output_value == "Binary":
            if input_text != "":
                self.output_text.setPlainText(hexadecimal_to_binary(input_text))
            else:
                self.output_text.setPlainText("")
        elif input_value == "Hexadecimal" and output_value == "Decimal":
            if input_text != "":
                self.output_text.setPlainText(str(hexadecimal_to_decimal(input_text)))
            else:
                self.output_text.setPlainText("")
        else:
            self.output_text.setPlainText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())