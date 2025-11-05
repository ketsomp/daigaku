"""
Flashcard review widget for Daigaku language learning app.
"""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QMessageBox, QComboBox, QGroupBox,
                             QProgressBar, QTextEdit)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from srs_algorithm import SRSAlgorithm
from add_card_dialog import AddCardDialog


class FlashcardWidget(QWidget):
    """Widget for flashcard review with SRS algorithm."""
    
    def __init__(self, db_manager, user_id, username=""):
        super().__init__()
        self.db_manager = db_manager
        self.user_id = user_id
        self.username = username
        self.current_deck = None
        self.cards = []
        self.current_card_index = 0
        self.current_card = None
        self.showing_answer = False
        self.srs = SRSAlgorithm()
        self.init_ui()
        self.load_decks()
    
    def init_ui(self):
        """Initialize the user interface."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Flashcard Review")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Deck selection
        deck_layout = QHBoxLayout()
        deck_layout.addWidget(QLabel("Select Deck:"))
        self.deck_combo = QComboBox()
        self.deck_combo.currentIndexChanged.connect(self.on_deck_changed)
        deck_layout.addWidget(self.deck_combo, 1)
        
        self.start_button = QPushButton("Start Review")
        self.start_button.clicked.connect(self.start_review)
        deck_layout.addWidget(self.start_button)
        
        # Add Card button (only for root user)
        if self.username == "root":
            self.add_card_button = QPushButton("➕ Add Card")
            self.add_card_button.setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    font-size: 12px;
                    font-weight: bold;
                    border: none;
                    border-radius: 5px;
                    padding: 5px 15px;
                }
                QPushButton:hover {
                    background-color: #0b7dda;
                }
            """)
            self.add_card_button.clicked.connect(self.open_add_card_dialog)
            deck_layout.addWidget(self.add_card_button)
        
        layout.addLayout(deck_layout)
        
        # Progress bar and Exit Review button container
        progress_layout = QHBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        progress_layout.addWidget(self.progress_bar, 1)
        
        # Exit Review button
        self.exit_review_button = QPushButton("⏹ Exit Review")
        self.exit_review_button.setFixedSize(120, 30)
        self.exit_review_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        self.exit_review_button.clicked.connect(self.exit_review)
        self.exit_review_button.setVisible(False)
        progress_layout.addWidget(self.exit_review_button)
        
        layout.addLayout(progress_layout)
        
        # Card display area
        self.card_group = QGroupBox()
        card_layout = QVBoxLayout()
        
        # Expression (front)
        self.expression_label = QLabel()
        self.expression_label.setFont(QFont("Arial", 32, QFont.Bold))
        self.expression_label.setAlignment(Qt.AlignCenter)
        self.expression_label.setMinimumHeight(100)
        self.expression_label.setStyleSheet("""
            background-color: #2d2d2d; 
            color: #ffffff;
            border-radius: 10px; 
            padding: 20px;
        """)
        card_layout.addWidget(self.expression_label)
        
        # Definition (back)
        self.definition_label = QLabel()
        self.definition_label.setFont(QFont("Arial", 16))
        self.definition_label.setAlignment(Qt.AlignCenter)
        self.definition_label.setWordWrap(True)
        self.definition_label.setVisible(False)
        card_layout.addWidget(self.definition_label)
        
        # Example sentence
        self.sentence_text = QTextEdit()
        self.sentence_text.setReadOnly(True)
        self.sentence_text.setMaximumHeight(100)
        self.sentence_text.setVisible(False)
        card_layout.addWidget(self.sentence_text)
        
        self.card_group.setLayout(card_layout)
        self.card_group.setVisible(False)
        layout.addWidget(self.card_group)
        
        # Show answer button
        self.show_answer_button = QPushButton("Show Answer")
        self.show_answer_button.setFixedHeight(50)
        self.show_answer_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        self.show_answer_button.clicked.connect(self.show_answer)
        self.show_answer_button.setVisible(False)
        layout.addWidget(self.show_answer_button)
        
        # Answer quality buttons
        self.answer_group = QGroupBox("How well did you know this?")
        answer_layout = QHBoxLayout()
        
        self.quality_buttons = []
        qualities = [
            ("1\nAgain", 1, "#f44336"),
            ("2\nHard", 2, "#FF9800"),
            ("3\nGood", 3, "#FFEB3B"),
            ("4\nEasy", 4, "#8BC34A"),
            ("5\nPerfect", 5, "#4CAF50")
        ]
        
        for label, quality, color in qualities:
            btn = QPushButton(label)
            btn.setFixedHeight(60)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: {"white" if quality <= 2 else "black"};
                    font-size: 12px;
                    font-weight: bold;
                    border: none;
                    border-radius: 5px;
                }}
                QPushButton:hover {{
                    opacity: 0.8;
                }}
            """)
            btn.clicked.connect(lambda checked, q=quality: self.record_answer(q))
            answer_layout.addWidget(btn)
            self.quality_buttons.append(btn)
        
        self.answer_group.setLayout(answer_layout)
        self.answer_group.setVisible(False)
        layout.addWidget(self.answer_group)
        
        # Statistics
        self.stats_label = QLabel()
        self.stats_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.stats_label)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def load_decks(self):
        """Load available decks from database."""
        decks = self.db_manager.get_all_decks()
        self.deck_combo.clear()
        for deck in decks:
            self.deck_combo.addItem(f"{deck['deck_name']} - {deck['description']}", deck['deck_id'])
    
    def on_deck_changed(self):
        """Handle deck selection change."""
        if self.deck_combo.currentIndex() >= 0:
            self.current_deck = self.deck_combo.currentData()
    
    def start_review(self):
        """Start reviewing flashcards."""
        if not self.current_deck:
            QMessageBox.warning(self, "No Deck", "Please select a deck first.")
            return
        
        self.cards = self.db_manager.get_cards_due_for_review(self.user_id, self.current_deck)
        
        if not self.cards:
            QMessageBox.information(self, "No Cards", "No cards available for review!")
            return
        
        self.current_card_index = 0
        self.card_group.setVisible(True)
        self.show_answer_button.setVisible(True)
        self.progress_bar.setVisible(True)
        self.exit_review_button.setVisible(True)
        self.progress_bar.setMaximum(len(self.cards))
        self.start_button.setEnabled(False)
        
        self.show_next_card()
    
    def show_next_card(self):
        """Display the next card."""
        if self.current_card_index >= len(self.cards):
            self.finish_review()
            return
        
        self.current_card = self.cards[self.current_card_index]
        self.showing_answer = False
        
        # Update display
        self.expression_label.setText(self.current_card['expression'])
        self.definition_label.setText("")
        self.definition_label.setVisible(False)
        self.sentence_text.setVisible(False)
        self.answer_group.setVisible(False)
        self.show_answer_button.setVisible(True)
        
        # Update progress
        self.progress_bar.setValue(self.current_card_index)
        self.stats_label.setText(f"Card {self.current_card_index + 1} of {len(self.cards)}")
    
    def show_answer(self):
        """Show the answer for the current card."""
        if not self.showing_answer:
            self.showing_answer = True
            self.definition_label.setText(f"📖 {self.current_card['expression_definition']}")
            self.definition_label.setVisible(True)
            
            # Show example sentence if available
            if self.current_card.get('japanese_sentence'):
                sentence_text = f"<b>Japanese:</b> {self.current_card['japanese_sentence']}<br>"
                sentence_text += f"<b>English:</b> {self.current_card['english_translation']}"
                self.sentence_text.setHtml(sentence_text)
                self.sentence_text.setVisible(True)
            
            self.show_answer_button.setVisible(False)
            self.answer_group.setVisible(True)
    
    def record_answer(self, quality):
        """Record the answer quality and move to next card."""
        if self.current_card:
            # Record review in database
            self.db_manager.record_card_review(
                self.user_id, 
                self.current_card['card_id'], 
                quality
            )
            
            # Move to next card
            self.current_card_index += 1
            self.show_next_card()
    
    def finish_review(self):
        """Finish the review session."""
        self.card_group.setVisible(False)
        self.answer_group.setVisible(False)
        self.show_answer_button.setVisible(False)
        self.progress_bar.setVisible(False)
        self.exit_review_button.setVisible(False)
        self.start_button.setEnabled(True)
        
        QMessageBox.information(self, "Review Complete", 
                              f"Great job! You reviewed {len(self.cards)} cards.\n"
                              f"Keep up the good work!")
        
        self.stats_label.setText("Select a deck and click 'Start Review' to begin.")
    
    def exit_review(self):
        """Exit the current review session and return to deck selection."""
        reply = QMessageBox.question(
            self,
            "Exit Review",
            f"Are you sure you want to exit?\n"
            f"You've reviewed {self.current_card_index} of {len(self.cards)} cards.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Reset review state
            self.card_group.setVisible(False)
            self.answer_group.setVisible(False)
            self.show_answer_button.setVisible(False)
            self.progress_bar.setVisible(False)
            self.exit_review_button.setVisible(False)
            self.start_button.setEnabled(True)
            self.current_card_index = 0
            self.cards = []
            self.current_card = None
            self.showing_answer = False
            
            self.stats_label.setText("Select a deck and click 'Start Review' to begin.")
            QMessageBox.information(self, "Review Exited", 
                                  "You can now select a different deck or start a new review.")
    
    def open_add_card_dialog(self):
        """Open dialog to add a new flashcard."""
        # Pass current deck as default (can be None), but allow user to select any deck
        dialog = AddCardDialog(self.db_manager, self.current_deck, self)
        if dialog.exec_() == AddCardDialog.Accepted:
            # Reload decks to update card counts
            self.load_decks()
            QMessageBox.information(self, "Success", 
                                  "Card added successfully! You can continue reviewing.")
