# 大学 Daigaku - Japanese Language Learning Application

A comprehensive Japanese language learning application built with Python and PyQt5, featuring flashcard review using the Spaced Repetition System (SRS) algorithm and immersion material tracking.

## Features

### 📇 Flashcard Review System

- **SRS Algorithm**: Intelligent spaced repetition for optimal learning
- **Multiple Decks**: Organize flashcards by topic or difficulty
- **Progress Tracking**: Monitor your learning progress
- **Rich Content**: Japanese expressions with definitions, example sentences, and translations

### 🎬 Immersion Material Tracking

- **Content Library**: Track books, movies, TV shows, and podcasts
- **Personal History**: Log materials you've consumed
- **Difficulty Ratings**: Filter by difficulty level (1-5 stars)
- **Admin Tools**: Add, edit, and delete materials (root user only)

### 🔐 User Authentication

- Secure login system with two user types:
  - **root**: Full admin access (add/delete materials)
  - **customer**: Standard user access

### 📊 Database Backend

- MySQL database with comprehensive schema
- Tracks user progress, reviews, and material history
- Supports multiple users and decks

## Installation

### Prerequisites

- Python 3.7 or higher
- MySQL Server 5.7 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**

   ```bash
   cd /Users/aniketsompura/Documents/Github/daigaku
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Set up the database**

   - Ensure MySQL server is running
   - Import the database schema:
     ```bash
     mysql -u root -p < /Users/aniketsompura/Downloads/dog.sql
     ```
   - This will create the `daigaku` database with all necessary tables

5. **Run the application**
   ```bash
   python3 main.py
   ```

## Usage

### Login

When you start the application, you'll see a login window:

1. **Database Connection**:

   - Host: `localhost` (default)
   - Database: `daigaku` (default)

2. **User Credentials**:
   - Username: `root` or `customer`
   - Password: Enter the password stored in the database

### Flashcard Review

1. Navigate to the **Flashcards** tab
2. Select a deck from the dropdown
3. Click **Start Review**
4. For each card:
   - Read the Japanese expression
   - Click **Show Answer** to reveal the definition
   - Rate your answer (1-5):
     - 1: Complete blackout
     - 2: Incorrect, but recognized
     - 3: Correct with difficulty
     - 4: Correct with hesitation
     - 5: Perfect recall
5. The SRS algorithm will schedule cards based on your performance

### Immersion Materials

1. Navigate to the **Immersion Materials** tab
2. View all available materials in the table
3. **Log materials**: Click the 📝 Log button to add to your history
4. **View history**: Click **My History** to see materials you've logged
5. **Admin only**: Add new materials or delete existing ones

## Database Schema

The application uses the following main tables:

- **user**: User accounts and profiles
- **deck**: Flashcard decks
- **flashcard**: Individual flashcards with Japanese content
- **user_card_review**: Review history with SRS data
- **immersion_material**: Library of immersion content
- **user_material_history**: User's immersion logs

## Project Structure

```
daigaku/
├── main.py                 # Application entry point
├── login_window.py         # Login dialog
├── main_window.py          # Main application window
├── flashcard_widget.py     # Flashcard review interface
├── immersion_widget.py     # Immersion materials interface
├── database.py             # Database operations
├── srs_algorithm.py        # Spaced Repetition System logic
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## SRS Algorithm

The application implements a modified SM-2 (SuperMemo 2) algorithm:

- **New cards**: Initially reviewed after 1 day
- **Quality ratings** determine the next interval:
  - Quality < 3: Reset to beginning
  - Quality ≥ 3: Increase interval based on ease factor
- **Intervals** gradually increase with successful reviews
- **Priority scoring** ensures difficult cards are reviewed more frequently

## Troubleshooting

### Database Connection Issues

- Ensure MySQL server is running: `mysql.server start`
- Verify database exists: `SHOW DATABASES;` in MySQL
- Check credentials are correct

### Module Not Found Errors

```bash
pip3 install PyQt5 mysql-connector-python
```

### PyQt5 Installation Issues on macOS

```bash
pip3 install --upgrade pip
pip3 install PyQt5
```

## Future Enhancements

- [ ] Audio playback for pronunciation
- [ ] Import/export flashcard decks
- [ ] Statistics dashboard
- [ ] Mobile app version
- [ ] Gamification features
- [ ] Community deck sharing

## License

This project is for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Credits

Built with:

- **PyQt5**: GUI framework
- **MySQL**: Database system
- **Python**: Programming language

---

**大学を楽しんでください！(Enjoy your studies!)**
