"""
PROJECT SUMMARY: Daigaku Language Learning Application
======================================================

OVERVIEW
--------
A comprehensive Japanese language learning application with flashcard review 
using Spaced Repetition System (SRS) and immersion material tracking.

TECHNOLOGY STACK
----------------
- Frontend: PyQt5 (Desktop GUI)
- Backend: Python 3.7+
- Database: MySQL 5.7+
- Algorithm: Modified SM-2 (SuperMemo 2) for SRS

PROJECT STRUCTURE
-----------------
daigaku/
├── main.py                    # Application entry point
├── login_window.py            # User authentication dialog
├── main_window.py             # Main application window with tabs
├── flashcard_widget.py        # Flashcard review interface
├── immersion_widget.py        # Immersion materials management
├── database.py                # Database operations and queries
├── srs_algorithm.py           # Spaced Repetition System logic
├── config.py                  # Configuration management
├── setup_check.py             # Setup verification utility
├── config.ini                 # Configuration file
├── requirements.txt           # Python dependencies
├── run.sh                     # Launch script
├── .gitignore                 # Git ignore rules
├── README.md                  # Full documentation
└── QUICKSTART.md              # Quick start guide

FEATURES IMPLEMENTED
--------------------

1. USER AUTHENTICATION
   - Login dialog with database configuration
   - Support for multiple users (root, customer)
   - Password-protected access
   - User role management (admin vs regular user)

2. FLASHCARD REVIEW SYSTEM
   - Browse available decks
   - Start review sessions
   - Display Japanese expressions with definitions
   - Show example sentences with translations
   - Quality rating system (1-5):
     * 1: Complete blackout
     * 2: Incorrect but recognized
     * 3: Correct with difficulty
     * 4: Correct with hesitation
     * 5: Perfect recall
   - Progress tracking during sessions
   - Review history storage

3. SRS ALGORITHM
   - Calculate next review intervals
   - Adjust difficulty based on performance
   - Priority scoring for card ordering
   - Reset poorly-recalled cards
   - Gradually increase intervals for well-known cards

4. IMMERSION MATERIALS
   - View all available materials
   - Filter by type (TV, movie, book, podcast)
   - Difficulty ratings (1-5 stars)
   - Length tracking (in minutes)
   - Log materials to personal history
   - View immersion history
   - Admin features:
     * Add new materials
     * Delete materials
     * Edit material details

5. USER INTERFACE
   - Clean, modern design
   - Tabbed interface for different features
   - Color-coded buttons for quality ratings
   - Progress bars for review sessions
   - Tables with sorting for materials
   - Responsive layouts
   - Status bar with user information

6. DATABASE INTEGRATION
   - Connection management
   - User authentication
   - Deck and flashcard retrieval
   - Review tracking
   - Material management
   - History logging
   - Transaction support

DATABASE SCHEMA
---------------
Tables:
- user: User accounts and profiles
- deck: Flashcard deck information
- flashcard: Individual flashcards with content
- user_card_review: Review history and SRS data
- immersion_material: Library of content
- user_material_history: User's immersion logs
- vocabulary: Vocabulary words
- word_meaning: Word definitions

KEY CLASSES
-----------

1. DatabaseManager (database.py)
   - connect() / disconnect()
   - authenticate_user()
   - get_all_decks()
   - get_flashcards_by_deck()
   - get_cards_due_for_review()
   - record_card_review()
   - get_all_immersion_materials()
   - add_material_to_history()
   - add_immersion_material()
   - delete_immersion_material()

2. SRSAlgorithm (srs_algorithm.py)
   - calculate_next_review_interval()
   - is_card_due()
   - get_card_priority()

3. LoginWindow (login_window.py)
   - Database connection configuration
   - User authentication
   - Login validation

4. MainWindow (main_window.py)
   - Tabbed interface
   - Menu bar
   - Status bar
   - User information display

5. FlashcardWidget (flashcard_widget.py)
   - Deck selection
   - Card display
   - Answer revelation
   - Quality rating
   - Progress tracking

6. ImmersionMaterialWidget (immersion_widget.py)
   - Material listing
   - Add/delete materials (admin)
   - Log materials
   - View history
   - Material details

DESIGN PATTERNS USED
--------------------
- MVC (Model-View-Controller): Separation of data, UI, and logic
- Singleton: Database connection management
- Factory: Widget creation
- Observer: PyQt5 signal/slot mechanism

USER WORKFLOWS
--------------

Flashcard Review:
1. User selects deck
2. Clicks "Start Review"
3. Views Japanese expression
4. Clicks "Show Answer"
5. Sees definition and example
6. Rates knowledge (1-5)
7. System records review
8. Next card shown
9. Session complete message

Immersion Tracking:
1. User views material library
2. Finds interesting content
3. Clicks "Log" button
4. Material added to history
5. Can view full history anytime

Admin Material Management:
1. Admin clicks "Add Material"
2. Fills in material details
3. Material added to database
4. Available to all users

CONFIGURATION
-------------
config.ini contains:
- Database connection details
- Default user list
- Application settings

SECURITY CONSIDERATIONS
-----------------------
- Passwords stored as hashes in database
- SQL injection prevention via parameterized queries
- User role validation
- Input sanitization

FUTURE ENHANCEMENTS
-------------------
- Audio pronunciation playback
- Import/export deck functionality
- Statistics dashboard
- Mobile app version
- Gamification elements
- Community deck sharing
- Multi-language support
- Offline mode
- Cloud sync

TESTING RECOMMENDATIONS
-----------------------
1. Unit tests for SRS algorithm
2. Database transaction tests
3. UI interaction tests
4. Login/authentication tests
5. Data validation tests

DEPLOYMENT NOTES
----------------
- Requires MySQL server running
- Database must be imported from dog.sql
- Python 3.7+ required
- PyQt5 and mysql-connector-python must be installed
- Virtual environment recommended

MAINTENANCE
-----------
- Regular database backups recommended
- Monitor review history table size
- Periodic cleanup of old sessions
- Update SRS parameters based on user feedback

PERFORMANCE
-----------
- Efficient database queries with indexes
- Lazy loading of card content
- Minimal UI redraws
- Connection pooling for database

ACCESSIBILITY
-------------
- Large, readable fonts
- Clear button labels
- Color-coded feedback
- Keyboard shortcuts supported

ERROR HANDLING
--------------
- Database connection failures
- Invalid user input
- Missing data
- Network issues
- SQL errors
- File access errors

SUCCESS METRICS
---------------
- User retention rate
- Cards reviewed per session
- Immersion materials logged
- Review consistency
- Learning progress

==========================================
Built with ❤️ for Japanese language learners
==========================================
"""
