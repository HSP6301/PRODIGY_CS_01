import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog, QDialogButtonBox
from PyQt5.QtGui import QClipboard

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Preserve case
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabetically
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetical characters are added as-is
            result += char

    return result

class CaesarCipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Caesar Cipher')

        # Layout
        layout = QVBoxLayout()

        # Message input
        self.message_label = QLabel('Enter your message:')
        self.message_input = QLineEdit(self)
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        # Shift input
        self.shift_label = QLabel('Enter shift value:')
        self.shift_input = QLineEdit(self)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_input)

        # Encrypt button
        self.encrypt_button = QPushButton('Encrypt', self)
        self.encrypt_button.clicked.connect(self.encrypt_message)
        layout.addWidget(self.encrypt_button)

        # Decrypt button
        self.decrypt_button = QPushButton('Decrypt', self)
        self.decrypt_button.clicked.connect(self.decrypt_message)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

    def validate_inputs(self):
        text = self.message_input.text()
        shift = self.shift_input.text()

        # Validate message input
        if not text.strip():
            QMessageBox.warning(self, 'Input Error', 'Message field is required.')
            return False

        # Validate shift input
        if not shift.isdigit():
            QMessageBox.warning(self, 'Input Error', 'Shift value must be a number.')
            return False

        return True

    def encrypt_message(self):
        if self.validate_inputs():
            text = self.message_input.text()
            shift = int(self.shift_input.text())
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            self.show_message_box('Encrypted Message', encrypted_text)

    def decrypt_message(self):
        if self.validate_inputs():
            text = self.message_input.text()
            shift = int(self.shift_input.text())
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            self.show_message_box('Decrypted Message', decrypted_text)

    def show_message_box(self, title, message):
        # Create a custom dialog box
        dialog = QDialog(self)
        dialog.setWindowTitle(title)

        # Layout
        layout = QVBoxLayout()

        # Message display
        label = QLabel(message, dialog)
        layout.addWidget(label)

        # Copy button
        copy_button = QPushButton('Copy', dialog)
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(message))
        layout.addWidget(copy_button)

        # Close button
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)

        dialog.setLayout(layout)
        dialog.exec_()

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CaesarCipherApp()
    ex.show()
    sys.exit(app.exec_())
