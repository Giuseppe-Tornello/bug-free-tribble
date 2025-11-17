import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QTextEdit, QVBoxLayout,
    QSizePolicy, QPushButton
)

class QuestionWindow(QWidget):
    def __init__(self, windowTitle, readonlyText):
        super().__init__()

        self.setWindowTitle(windowTitle)
        self.resize(600, 400)

        layout = QVBoxLayout()

        # --- text di sola lettura ---
        self.readonly_box = QTextEdit()
        self.readonly_box.setReadOnly(True)
        self.readonly_box.setText(readonlyText)
        self.readonly_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # --- Casella modificabile ---
        self.user_box = QTextEdit()
        self.user_box.setPlaceholderText("Scrivi qui...")
        self.user_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # --- Pulsante INVIO ---
        self.button = QPushButton("Invio")
        self.button.setDefault(True)
        self.button.clicked.connect(self.on_submit)

        # Aggiunge i widget al layout
        layout.addWidget(self.readonly_box)
        layout.addWidget(self.user_box)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_submit(self):
        """Stampa il text dell'utente e chiude la QuestionWindow."""
        text = self.user_box.toPlainText()
        print("text INSERITO DALL'UTENTE:")
        print(text)
        self.close()

    def getUserText(self):
        """Ritorna il text dell'utente (se ti serve altrove)."""
        return self.user_box.toPlainText()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    text = "aòlsalklasakskasmasaskalksal"

    QuestionWindow = QuestionWindow("Nome finestra", text)
    QuestionWindow.show()

    sys.exit(app.exec())
