"""
Dialog for adding new flashcards to a deck.
"""
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QTextEdit, QPushButton, QComboBox,
                             QMessageBox, QGroupBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class AddCardDialog(QDialog):
    """Dialog for adding new flashcards."""
    
    def __init__(self, db_manager, deck_id=None, parent=None):
        super().__init__(parent)
        self.db_manager = db_manager
        self.selected_deck_id = deck_id
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Add New Flashcard")
        self.setFixedSize(600, 600)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Add New Flashcard")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Deck Selection Group
        deck_group = QGroupBox("Select Deck")
        deck_layout = QVBoxLayout()
        
        deck_selection_layout = QHBoxLayout()
        deck_label = QLabel("Add to Deck:")
        deck_label.setFont(QFont("Arial", 10, QFont.Bold))
        deck_selection_layout.addWidget(deck_label)
        
        self.deck_combo = QComboBox()
        self.deck_combo.setFont(QFont("Arial", 10))
        self.load_decks()
        deck_selection_layout.addWidget(self.deck_combo, 1)
        
        deck_layout.addLayout(deck_selection_layout)
        deck_group.setLayout(deck_layout)
        layout.addWidget(deck_group)
        
        # Card Information Group
        card_group = QGroupBox("Card Information")
        card_layout = QVBoxLayout()
        
        # Expression (Front)
        expression_layout = QVBoxLayout()
        expression_label = QLabel("Expression (Front of card):")
        expression_label.setFont(QFont("Arial", 10, QFont.Bold))
        expression_layout.addWidget(expression_label)
        self.expression_input = QLineEdit()
        self.expression_input.setPlaceholderText("e.g., 日本語")
        self.expression_input.setFont(QFont("Arial", 14))
        expression_layout.addWidget(self.expression_input)
        card_layout.addLayout(expression_layout)
        
        # Definition (Back)
        definition_layout = QVBoxLayout()
        definition_label = QLabel("Definition (Back of card):")
        definition_label.setFont(QFont("Arial", 10, QFont.Bold))
        definition_layout.addWidget(definition_label)
        self.definition_input = QTextEdit()
        self.definition_input.setPlaceholderText("e.g., Japanese language")
        self.definition_input.setMaximumHeight(80)
        definition_layout.addWidget(self.definition_input)
        card_layout.addLayout(definition_layout)
        
        # Japanese Sentence (Optional)
        sentence_layout = QVBoxLayout()
        sentence_label = QLabel("Example Sentence (Japanese) - Optional:")
        sentence_label.setFont(QFont("Arial", 10, QFont.Bold))
        sentence_layout.addWidget(sentence_label)
        self.japanese_sentence_input = QTextEdit()
        self.japanese_sentence_input.setPlaceholderText("e.g., 私は日本語を勉強しています。")
        self.japanese_sentence_input.setMaximumHeight(60)
        sentence_layout.addWidget(self.japanese_sentence_input)
        card_layout.addLayout(sentence_layout)
        
        # English Translation (Optional)
        translation_layout = QVBoxLayout()
        translation_label = QLabel("English Translation - Optional:")
        translation_label.setFont(QFont("Arial", 10, QFont.Bold))
        translation_layout.addWidget(translation_label)
        self.english_translation_input = QTextEdit()
        self.english_translation_input.setPlaceholderText("e.g., I am studying Japanese.")
        self.english_translation_input.setMaximumHeight(60)
        translation_layout.addWidget(self.english_translation_input)
        card_layout.addLayout(translation_layout)
        
        card_group.setLayout(card_layout)
        layout.addWidget(card_group)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        cancel_button = QPushButton("Cancel")
        cancel_button.setFixedHeight(40)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        save_button = QPushButton("Save Card")
        save_button.setFixedHeight(40)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        save_button.clicked.connect(self.save_card)
        button_layout.addWidget(save_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def load_decks(self):
        """Load available decks from database."""
        decks = self.db_manager.get_all_decks()
        self.deck_combo.clear()
        
        for deck in decks:
            self.deck_combo.addItem(
                f"{deck['deck_name']} - {deck['description']}", 
                deck['deck_id']
            )
        
        # If a deck was pre-selected, set it
        if self.selected_deck_id:
            for i in range(self.deck_combo.count()):
                if self.deck_combo.itemData(i) == self.selected_deck_id:
                    self.deck_combo.setCurrentIndex(i)
                    break
    
    def save_card(self):
        """Validate and save the new flashcard."""
        # Get selected deck
        if self.deck_combo.currentIndex() < 0:
            QMessageBox.warning(self, "Validation Error", "Please select a deck!")
            return
        
        deck_id = self.deck_combo.currentData()
        expression = self.expression_input.text().strip()
        definition = self.definition_input.toPlainText().strip()
        japanese_sentence = self.japanese_sentence_input.toPlainText().strip()
        english_translation = self.english_translation_input.toPlainText().strip()
        
        # Validation
        if not expression:
            QMessageBox.warning(self, "Validation Error", "Expression field is required!")
            self.expression_input.setFocus()
            return
        
        if not definition:
            QMessageBox.warning(self, "Validation Error", "Definition field is required!")
            self.definition_input.setFocus()
            return
        
        # Save to database
        success = self.db_manager.add_flashcard(
            deck_id=deck_id,
            expression=expression,
            definition=definition,
            japanese_sentence=japanese_sentence if japanese_sentence else None,
            english_translation=english_translation if english_translation else None
        )
        
        if success:
            QMessageBox.information(self, "Success", 
                                  f"Flashcard added successfully to {self.deck_combo.currentText()}!")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Failed to add flashcard to database.")
