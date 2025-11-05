"""
Main application window for Daigaku language learning app.
"""
from PyQt5.QtWidgets import (QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QAction, QMessageBox, QStatusBar, QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from flashcard_widget import FlashcardWidget
from immersion_widget import ImmersionMaterialWidget


class MainWindow(QMainWindow):
    """Main application window with tabbed interface."""
    
    def __init__(self, db_manager, user_id, username):
        super().__init__()
        self.db_manager = db_manager
        self.user_id = user_id
        self.username = username
        self.init_ui()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle(f"Daigaku - Language Learning ({self.username})")
        self.setGeometry(100, 100, 1000, 700)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create status bar
        self.statusBar().showMessage(f"Logged in as: {self.username}")
        
        # Create central widget with tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Header with exit button
        header_layout = QHBoxLayout()
        
        # Welcome header
        header = QLabel(f"Welcome to 大学 Daigaku, {self.username}!")
        header.setFont(QFont("Arial", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("""
            padding: 10px; 
            background-color: #2d2d2d; 
            color: #ffffff;
            border-radius: 5px;
        """)
        header_layout.addWidget(header, 1)
        
        # Exit button
        exit_button = QPushButton("✕ Exit")
        exit_button.setFixedSize(80, 40)
        exit_button.setStyleSheet("""
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
            QPushButton:pressed {
                background-color: #c41c0c;
            }
        """)
        exit_button.clicked.connect(self.close)
        header_layout.addWidget(exit_button)
        
        layout.addLayout(header_layout)
        
        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #cccccc;
                border-radius: 5px;
                margin-top: 10px;
            }
            QTabBar::tab {
                padding: 15px 80px;
                font-size: 16px;
                font-weight: bold;
                margin-right: 30px;
                min-width: 200px;
                border-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: #4CAF50;
                color: white;
            }
            QTabBar::tab:hover {
                background-color: #5a5a5a;
                color: white;
            }
            QTabBar::tab:!selected {
                background-color: #3a3a3a;
                color: #ffffff;
                margin-top: 2px;
            }
        """)
        
        # Create tabs
        self.flashcard_widget = FlashcardWidget(self.db_manager, self.user_id, self.username)
        self.tabs.addTab(self.flashcard_widget, "📇 Flashcards")
        
        self.immersion_widget = ImmersionMaterialWidget(self.db_manager, self.user_id, self.username)
        self.tabs.addTab(self.immersion_widget, "🎬 Immersion Materials")
        
        layout.addWidget(self.tabs)
        
        central_widget.setLayout(layout)
        
        # Show user info
        self.load_user_info()
    
    def create_menu_bar(self):
        """Create the menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        refresh_action = QAction("&Refresh", self)
        refresh_action.setShortcut("F5")
        refresh_action.triggered.connect(self.refresh_all)
        file_menu.addAction(refresh_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        user_info_action = QAction("&User Info", self)
        user_info_action.triggered.connect(self.show_user_info)
        help_menu.addAction(user_info_action)
    
    def refresh_all(self):
        """Refresh all data."""
        if hasattr(self.flashcard_widget, 'load_decks'):
            self.flashcard_widget.load_decks()
        if hasattr(self.immersion_widget, 'load_materials'):
            self.immersion_widget.load_materials()
        self.statusBar().showMessage("Data refreshed!", 3000)
    
    def load_user_info(self):
        """Load and display user information."""
        user_info = self.db_manager.get_user_info(self.user_id)
        if user_info:
            status_msg = f"Logged in as: {self.username} | Level: {user_info.get('current_level', 'N/A')} | "
            status_msg += f"Vocabulary: {user_info.get('vocabulary_learnt', 0)}"
            self.statusBar().showMessage(status_msg)
    
    def show_user_info(self):
        """Show detailed user information."""
        user_info = self.db_manager.get_user_info(self.user_id)
        if user_info:
            info_text = f"""
            <h2>User Information</h2>
            <table>
            <tr><td><b>Username:</b></td><td>{user_info['username']}</td></tr>
            <tr><td><b>Email:</b></td><td>{user_info['email']}</td></tr>
            <tr><td><b>Current Level:</b></td><td>{user_info['current_level']}</td></tr>
            <tr><td><b>Vocabulary Learnt:</b></td><td>{user_info['vocabulary_learnt']}</td></tr>
            <tr><td><b>Date Joined:</b></td><td>{user_info['date_joined']}</td></tr>
            </table>
            """
            
            msg = QMessageBox(self)
            msg.setWindowTitle("User Information")
            msg.setTextFormat(Qt.RichText)
            msg.setText(info_text)
            msg.exec_()
    
    def show_about(self):
        """Show about dialog."""
        about_text = """
        <h2>大学 Daigaku</h2>
        <h3>Japanese Language Learning System</h3>
        <p><b>Version:</b> 1.0.0</p>
        <p><b>Features:</b></p>
        <ul>
        <li>📇 Flashcard review with SRS algorithm</li>
        <li>🎬 Immersion material tracking</li>
        <li>📊 Progress tracking</li>
        <li>🗄️ SQL database backend</li>
        </ul>
        <p><i>Built with Python and PyQt5</i></p>
        """
        
        msg = QMessageBox(self)
        msg.setWindowTitle("About Daigaku")
        msg.setTextFormat(Qt.RichText)
        msg.setText(about_text)
        msg.exec_()
    
    def closeEvent(self, event):
        """Handle window close event."""
        reply = QMessageBox.question(
            self,
            "Exit Confirmation",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            # Close database connection
            if self.db_manager:
                self.db_manager.disconnect()
            event.accept()
        else:
            event.ignore()
