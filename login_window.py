"""
Login window for Daigaku language learning app.
"""
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QMessageBox, QGroupBox, QComboBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import DatabaseManager


class LoginWindow(QDialog):
    """Login dialog for user authentication."""
    
    def __init__(self):
        super().__init__()
        self.db_manager = None
        self.user_id = None
        self.username = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Daigaku - Login")
        self.setFixedSize(600, 700)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Title
        title = QLabel("大学 Daigaku")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        subtitle = QLabel("Language Learning System")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: gray;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(20)
        
        # Database Connection Group
        db_group = QGroupBox("Database Connection")
        db_layout = QVBoxLayout()
        
        # Host
        host_layout = QHBoxLayout()
        host_layout.addWidget(QLabel("Host:"))
        self.host_input = QLineEdit()
        self.host_input.setText("localhost")
        host_layout.addWidget(self.host_input)
        db_layout.addLayout(host_layout)
        
        # Database name
        dbname_layout = QHBoxLayout()
        dbname_layout.addWidget(QLabel("Database:"))
        self.dbname_input = QLineEdit()
        self.dbname_input.setText("daigaku")
        dbname_layout.addWidget(self.dbname_input)
        db_layout.addLayout(dbname_layout)
        
        db_group.setLayout(db_layout)
        layout.addWidget(db_group)
        
        # Login Group
        login_group = QGroupBox("User Login")
        login_layout = QVBoxLayout()
        
        # Username (preset options)
        username_layout = QHBoxLayout()
        username_layout.addWidget(QLabel("Username:"))
        self.username_combo = QComboBox()
        self.username_combo.addItems(["root", "customer"])
        self.username_combo.setEditable(True)
        username_layout.addWidget(self.username_combo)
        login_layout.addLayout(username_layout)
        
        # Password
        password_layout = QHBoxLayout()
        password_layout.addWidget(QLabel("Password:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.returnPressed.connect(self.handle_login)
        password_layout.addWidget(self.password_input)
        login_layout.addLayout(password_layout)
        
        login_group.setLayout(login_layout)
        layout.addWidget(login_group)
        
        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.setFixedHeight(40)
        self.login_button.setStyleSheet("""
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
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.login_button.clicked.connect(self.handle_login)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
    
    def handle_login(self):
        """Handle login button click."""
        host = self.host_input.text().strip()
        database = self.dbname_input.text().strip()
        username = self.username_combo.currentText().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password.")
            return
        
        # Create database manager and connect
        self.db_manager = DatabaseManager(host=host, database=database, user='root', password='root', unix_socket='/tmp/mysql.sock')
        
        if not self.db_manager.connect():
            QMessageBox.critical(self, "Connection Error", 
                               "Failed to connect to the database.\nPlease check your connection settings.")
            return
        
        # Authenticate user
        user_id = self.db_manager.authenticate_user(username, password)
        
        if user_id:
            self.user_id = user_id
            self.username = username
            QMessageBox.information(self, "Success", f"Welcome, {username}!")
            self.accept()  # Close dialog with success
        else:
            QMessageBox.warning(self, "Login Failed", 
                              "Invalid username or password.\nPlease try again.")
            self.password_input.clear()
            self.password_input.setFocus()
