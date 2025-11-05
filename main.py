"""
Daigaku - Japanese Language Learning Application
Main entry point for the application.
"""
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QFont
from login_window import LoginWindow
from main_window import MainWindow


def main():
    """Main application entry point."""
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Daigaku")
    
    # Set default font
    app.setFont(QFont("Arial", 10))
    
    # Show login window
    login = LoginWindow()
    
    if login.exec_() == LoginWindow.Accepted:
        # Login successful, show main window
        if login.db_manager and login.user_id:
            main_window = MainWindow(
                db_manager=login.db_manager,
                user_id=login.user_id,
                username=login.username
            )
            main_window.show()
            sys.exit(app.exec_())
        else:
            QMessageBox.critical(None, "Error", "Failed to initialize application.")
            sys.exit(1)
    else:
        # Login cancelled
        sys.exit(0)


if __name__ == "__main__":
    main()
