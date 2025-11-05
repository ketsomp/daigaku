"""
Immersion material widget for Daigaku language learning app.
"""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QMessageBox, QTableWidget, QTableWidgetItem,
                             QHeaderView, QDialog, QLineEdit, QSpinBox, QComboBox,
                             QFormLayout, QDialogButtonBox, QGroupBox, QTextEdit,
                             QAbstractItemView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class AddMaterialDialog(QDialog):
    """Dialog for adding new immersion material."""
    
    def __init__(self, parent=None, next_id=1):
        super().__init__(parent)
        self.next_id = next_id
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Add Immersion Material")
        self.setMinimumWidth(400)
        
        layout = QFormLayout()
        
        # Material ID (auto-generated)
        self.id_label = QLabel(str(self.next_id))
        layout.addRow("Material ID:", self.id_label)
        
        # Title
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter material title")
        layout.addRow("Title:*", self.title_input)
        
        # Type
        self.type_combo = QComboBox()
        self.type_combo.addItems(["television", "movie", "book", "podcast"])
        layout.addRow("Type:*", self.type_combo)
        
        # Source
        self.source_input = QLineEdit()
        self.source_input.setPlaceholderText("e.g., Netflix, Amazon, etc.")
        layout.addRow("Source:", self.source_input)
        
        # URL
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Purchase/streaming URL")
        layout.addRow("URL:", self.url_input)
        
        # Length
        self.length_input = QSpinBox()
        self.length_input.setRange(0, 10000)
        self.length_input.setSuffix(" min")
        layout.addRow("Length:", self.length_input)
        
        # Difficulty
        self.difficulty_input = QSpinBox()
        self.difficulty_input.setRange(1, 5)
        self.difficulty_input.setValue(3)
        layout.addRow("Difficulty (1-5):", self.difficulty_input)
        
        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.validate_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)
        
        self.setLayout(layout)
    
    def validate_and_accept(self):
        """Validate input and accept dialog."""
        if not self.title_input.text().strip():
            QMessageBox.warning(self, "Validation Error", "Title is required!")
            return
        self.accept()
    
    def get_data(self):
        """Get the entered data."""
        return {
            'material_id': self.next_id,
            'title': self.title_input.text().strip(),
            'type': self.type_combo.currentText(),
            'source': self.source_input.text().strip() or None,
            'url': self.url_input.text().strip() or None,
            'length': self.length_input.value() if self.length_input.value() > 0 else None,
            'avg_difficulty': self.difficulty_input.value()
        }


class ImmersionMaterialWidget(QWidget):
    """Widget for managing immersion materials."""
    
    def __init__(self, db_manager, user_id, username):
        super().__init__()
        self.db_manager = db_manager
        self.user_id = user_id
        self.username = username
        self.is_admin = (username == 'root')
        self.init_ui()
        self.load_materials()
    
    def init_ui(self):
        """Initialize the user interface."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Immersion Materials")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Info text
        info = QLabel("Track your immersion with Japanese content")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: gray; margin-bottom: 10px;")
        layout.addWidget(info)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        self.refresh_button = QPushButton("🔄 Refresh")
        self.refresh_button.clicked.connect(self.load_materials)
        button_layout.addWidget(self.refresh_button)
        
        if self.is_admin:
            self.add_button = QPushButton("➕ Add Material")
            self.add_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    font-weight: bold;
                    padding: 5px 15px;
                    border: none;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            self.add_button.clicked.connect(self.add_material)
            button_layout.addWidget(self.add_button)
        
        button_layout.addStretch()
        
        self.view_history_button = QPushButton("📚 My History")
        self.view_history_button.clicked.connect(self.view_history)
        button_layout.addWidget(self.view_history_button)
        
        layout.addLayout(button_layout)
        
        # Materials table
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "ID", "Title", "Type", "Source", "Length (min)", "Difficulty", "Actions"
        ])
        
        # Table styling
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        
        layout.addWidget(self.table)
        
        # Statistics
        self.stats_label = QLabel()
        self.stats_label.setAlignment(Qt.AlignCenter)
        self.stats_label.setStyleSheet("font-size: 12px; color: gray; margin-top: 10px;")
        layout.addWidget(self.stats_label)
        
        self.setLayout(layout)
    
    def load_materials(self):
        """Load immersion materials from database."""
        materials = self.db_manager.get_all_immersion_materials()
        
        self.table.setRowCount(len(materials))
        
        for row, material in enumerate(materials):
            # ID
            self.table.setItem(row, 0, QTableWidgetItem(str(material['material_id'])))
            
            # Title
            self.table.setItem(row, 1, QTableWidgetItem(material['title']))
            
            # Type
            type_item = QTableWidgetItem(material['type'].capitalize())
            type_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 2, type_item)
            
            # Source
            source = material.get('source', '') or '-'
            self.table.setItem(row, 3, QTableWidgetItem(source))
            
            # Length
            length = str(material.get('length', '')) if material.get('length') else '-'
            length_item = QTableWidgetItem(length)
            length_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 4, length_item)
            
            # Difficulty
            difficulty = '⭐' * (material.get('average_difficulty', 0) or 0)
            difficulty_item = QTableWidgetItem(difficulty)
            difficulty_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 5, difficulty_item)
            
            # Actions
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.setContentsMargins(2, 2, 2, 2)
            
            # Log button
            log_btn = QPushButton("📝 Log")
            log_btn.setStyleSheet("padding: 2px 8px;")
            log_btn.clicked.connect(lambda checked, m_id=material['material_id']: self.log_material(m_id))
            action_layout.addWidget(log_btn)
            
            # Delete button (admin only)
            if self.is_admin:
                delete_btn = QPushButton("🗑️")
                delete_btn.setStyleSheet("background-color: #f44336; color: white; padding: 2px 8px;")
                delete_btn.clicked.connect(lambda checked, m_id=material['material_id']: self.delete_material(m_id))
                action_layout.addWidget(delete_btn)
            
            action_layout.addStretch()
            self.table.setCellWidget(row, 6, action_widget)
        
        self.stats_label.setText(f"Total Materials: {len(materials)}")
    
    def add_material(self):
        """Add new immersion material."""
        # Get next ID
        materials = self.db_manager.get_all_immersion_materials()
        next_id = max([m['material_id'] for m in materials], default=0) + 1
        
        dialog = AddMaterialDialog(self, next_id)
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.get_data()
            success = self.db_manager.add_immersion_material(
                material_id=data['material_id'],
                title=data['title'],
                material_type=data['type'],
                source=data['source'],
                length=data['length'],
                avg_difficulty=data['avg_difficulty'],
                url=data['url']
            )
            
            if success:
                QMessageBox.information(self, "Success", "Material added successfully!")
                self.load_materials()
            else:
                QMessageBox.critical(self, "Error", "Failed to add material.")
    
    def delete_material(self, material_id):
        """Delete an immersion material."""
        reply = QMessageBox.question(
            self, 
            "Confirm Delete",
            f"Are you sure you want to delete material ID {material_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if self.db_manager.delete_immersion_material(material_id):
                QMessageBox.information(self, "Success", "Material deleted successfully!")
                self.load_materials()
            else:
                QMessageBox.critical(self, "Error", "Failed to delete material.")
    
    def log_material(self, material_id):
        """Log material to user's history."""
        success = self.db_manager.add_material_to_history(self.user_id, material_id)
        
        if success:
            QMessageBox.information(self, "Success", "Material logged to your history!")
        else:
            QMessageBox.warning(self, "Error", "Failed to log material. It may already be in your history.")
    
    def view_history(self):
        """View user's material history."""
        history = self.db_manager.get_user_material_history(self.user_id)
        
        if not history:
            QMessageBox.information(self, "History", "You haven't logged any materials yet!")
            return
        
        # Create dialog to show history
        dialog = QDialog(self)
        dialog.setWindowTitle("My Immersion History")
        dialog.setMinimumSize(600, 400)
        
        layout = QVBoxLayout()
        
        title = QLabel(f"📚 {self.username}'s Immersion History")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # History table
        history_table = QTableWidget()
        history_table.setColumnCount(4)
        history_table.setHorizontalHeaderLabels(["Title", "Type", "Length", "Difficulty"])
        history_table.setRowCount(len(history))
        
        for row, item in enumerate(history):
            history_table.setItem(row, 0, QTableWidgetItem(item['title']))
            history_table.setItem(row, 1, QTableWidgetItem(item['type'].capitalize()))
            
            length = str(item.get('length', '')) if item.get('length') else '-'
            history_table.setItem(row, 2, QTableWidgetItem(length))
            
            difficulty = '⭐' * (item.get('average_difficulty', 0) or 0)
            history_table.setItem(row, 3, QTableWidgetItem(difficulty))
        
        history_table.setAlternatingRowColors(True)
        history_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        layout.addWidget(history_table)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        
        dialog.setLayout(layout)
        dialog.exec_()
