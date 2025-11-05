"""
Database connection and operations module for Daigaku language learning app.
"""
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
import hashlib


class DatabaseManager:
    """Manages all database connections and operations."""
    
    def __init__(self, host='localhost', database='daigaku', user='root', password='root', unix_socket='/tmp/mysql.sock'):
        """Initialize database connection parameters."""
        self.host = host
        self.database = database
        self.user = 'root'
        self.password = 'scross'
        self.unix_socket = unix_socket
        self.connection = None
    
    def connect(self):
        """Establish connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                unix_socket=self.unix_socket,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def disconnect(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def authenticate_user(self, username, password):
        """
        Authenticate user credentials.
        Returns user_id if successful, None otherwise.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            # For simplicity, checking username against password_hash
            # In production, you'd hash the password properly
            query = "SELECT user_id, username FROM user WHERE username = %s AND password_hash = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.close()
            return result['user_id'] if result else None
        except Error as e:
            print(f"Authentication error: {e}")
            return None
    
    def get_user_info(self, user_id):
        """Get user information."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM user WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching user info: {e}")
            return None
    
    # ========== FLASHCARD METHODS ==========
    
    def get_all_decks(self):
        """Get all available decks."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM deck ORDER BY deck_id"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching decks: {e}")
            return []
    
    def get_flashcards_by_deck(self, deck_id):
        """Get all flashcards from a specific deck."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM flashcard WHERE deck_id = %s"
            cursor.execute(query, (deck_id,))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching flashcards: {e}")
            return []
    
    def add_flashcard(self, deck_id, expression, definition, japanese_sentence=None, english_translation=None):
        """Add a new flashcard to a deck."""
        try:
            cursor = self.connection.cursor()
            # Get next card_id
            cursor.execute("SELECT COALESCE(MAX(card_id), 0) + 1 as next_id FROM flashcard")
            card_id = cursor.fetchone()[0]
            
            query = """
                INSERT INTO flashcard (card_id, deck_id, expression, expression_definition, 
                                     japanese_sentence, english_translation)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (card_id, deck_id, expression, definition, 
                                 japanese_sentence, english_translation))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding flashcard: {e}")
            return False
    
    def get_cards_due_for_review(self, user_id, deck_id):
        """
        Get cards that are due for review based on SRS algorithm.
        Returns cards that haven't been reviewed or need review.
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
                SELECT f.*, 
                       ucr.review_date, 
                       ucr.answer_quality,
                       DATEDIFF(CURDATE(), ucr.review_date) as days_since_review
                FROM flashcard f
                LEFT JOIN user_card_review ucr ON f.card_id = ucr.card_id AND ucr.user_id = %s
                WHERE f.deck_id = %s
                ORDER BY ucr.review_date ASC, f.card_id
            """
            cursor.execute(query, (user_id, deck_id))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching cards due for review: {e}")
            return []
    
    def record_card_review(self, user_id, card_id, answer_quality):
        """
        Record a flashcard review.
        answer_quality: 1-5 (1=complete blackout, 5=perfect response)
        """
        try:
            cursor = self.connection.cursor()
            # Get next review_id
            cursor.execute("SELECT COALESCE(MAX(review_id), 0) + 1 as next_id FROM user_card_review")
            review_id = cursor.fetchone()[0]
            
            query = """
                INSERT INTO user_card_review (review_id, user_id, card_id, review_date, answer_quality, time_taken)
                VALUES (%s, %s, %s, CURDATE(), %s, NOW())
            """
            cursor.execute(query, (review_id, user_id, card_id, answer_quality))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error recording review: {e}")
            return False
    
    def get_card_review_history(self, user_id, card_id):
        """Get review history for a specific card."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
                SELECT * FROM user_card_review 
                WHERE user_id = %s AND card_id = %s 
                ORDER BY review_date DESC
            """
            cursor.execute(query, (user_id, card_id))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching review history: {e}")
            return []
    
    # ========== IMMERSION MATERIAL METHODS ==========
    
    def get_all_immersion_materials(self):
        """Get all immersion materials."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM immersion_material ORDER BY material_id"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching immersion materials: {e}")
            return []
    
    def get_user_material_history(self, user_id):
        """Get user's immersion material history."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
                SELECT umh.*, im.title, im.type, im.length, im.average_difficulty
                FROM user_material_history umh
                JOIN immersion_material im ON umh.material_id = im.material_id
                WHERE umh.user_id = %s
                ORDER BY umh.history_id DESC
            """
            cursor.execute(query, (user_id,))
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching material history: {e}")
            return []
    
    def add_material_to_history(self, user_id, material_id, saved_for_later=None):
        """Add material to user's history."""
        try:
            cursor = self.connection.cursor()
            # Get next history_id
            cursor.execute("SELECT COALESCE(MAX(history_id), 0) + 1 as next_id FROM user_material_history")
            history_id = cursor.fetchone()[0]
            
            query = """
                INSERT INTO user_material_history (history_id, user_id, material_id, saved_for_later)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (history_id, user_id, material_id, saved_for_later))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding material to history: {e}")
            return False
    
    def add_immersion_material(self, material_id, title, material_type, source=None, 
                              length=None, avg_difficulty=None, url=None):
        """Add new immersion material."""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO immersion_material 
                (material_id, title, purchase_website_url, type, source, length, average_difficulty)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (material_id, title, url, material_type, source, length, avg_difficulty))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error adding immersion material: {e}")
            return False
    
    def delete_immersion_material(self, material_id):
        """Delete an immersion material."""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM immersion_material WHERE material_id = %s"
            cursor.execute(query, (material_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error deleting material: {e}")
            return False
    
    def update_immersion_material(self, material_id, **kwargs):
        """Update immersion material fields."""
        try:
            cursor = self.connection.cursor()
            # Build dynamic update query
            set_clause = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            values = list(kwargs.values())
            values.append(material_id)
            
            query = f"UPDATE immersion_material SET {set_clause} WHERE material_id = %s"
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error updating material: {e}")
            return False
