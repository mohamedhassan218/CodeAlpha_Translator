"""
    Module contains simple UI to our translator.
     
    @author  Mohamed Hassan
    @since   2024-5-2
"""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QTextEdit,
)

# from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from translator import translate


def test_translate(text, x, y):
    # A function just to test the logic.
    return f"Translation from {x} to {y}."


class TranslatorApp(QWidget):
    """
    Class that represents our UI element to abstract
    the details of the code.
    
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setStyleSheet("background-color: #E0FFFF;")

        # Create a label for the text input field.
        self.label = QLabel("Enter text:")
        layout.addWidget(self.label)

        # Create a text input field.
        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        # Create a label for the "from" language dropdown menu.
        self.from_lang_label = QLabel("From Language:")
        layout.addWidget(self.from_lang_label)

        # Create a dropdown menu with language options for translation source.
        self.from_lang_combo = QComboBox()
        self.from_lang_combo.addItems(["English", "French", "Arabic", "German"])
        layout.addWidget(self.from_lang_combo)

        # Create a label for the "to" language dropdown menu.
        self.to_lang_label = QLabel("To Language:")
        layout.addWidget(self.to_lang_label)

        # Create a dropdown menu with language options for translation target.
        self.to_lang_combo = QComboBox()
        self.to_lang_combo.addItems(["English", "French", "Arabic", "German"])
        layout.addWidget(self.to_lang_combo)

        # Create a button to process the translation.
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet("QPushButton { font-size: 12px; }")
        self.translate_button.clicked.connect(self.translate_text)
        layout.addWidget(self.translate_button, alignment=Qt.AlignCenter)

        # Create a text area for displaying the translation result.
        self.result_text_area = QTextEdit()
        self.result_text_area.setReadOnly(True)
        layout.addWidget(self.result_text_area)

        self.setLayout(layout)

    def translate_text(self):
        # Get the text to be translated.
        text = self.entry.text()

        # Language mappings for translation.
        from_lang_map = {
            "English": "en",
            "French": "fr",
            "Arabic": "ar",
            "German": "de",
        }
        to_lang_map = {"English": "en", "French": "fr", "Arabic": "ar", "German": "de"}

        # Test our work . . .
        translation = test_translate(
            text,
            from_lang_map[self.from_lang_combo.currentText()],
            to_lang_map[self.to_lang_combo.currentText()],
        )
        self.result_text_area.setText(translation)

        # Perform the translation using the selected languages and the text entered.
        # translation = translate(text, from_lang_map[self.from_lang_combo.currentText()], to_lang_map[self.to_lang_combo.currentText()])

        # Set the translated text in the result text area.
        # self.result_text_area.setText(translation[0]['translations'][0]['text'])


app = QApplication(sys.argv)
translator = TranslatorApp()
translator.show()
sys.exit(app.exec_())
