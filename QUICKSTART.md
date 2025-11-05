# Quick Start Guide - Daigaku

## 🚀 Getting Started in 5 Minutes

### Step 1: Verify Prerequisites

```bash
# Check Python version (need 3.7+)
python3 --version

# Check MySQL is running
mysql.server status
# If not running, start it:
mysql.server start
```

### Step 2: Set Up Database

```bash
# Import the database schema from dog.sql
mysql -u root -p < /Users/aniketsompura/Downloads/dog.sql
# Press Enter if no password is set, or enter your MySQL root password
```

### Step 3: Install Dependencies

```bash
# Navigate to project directory
cd /Users/aniketsompura/Documents/Github/daigaku

# Install required packages (already done if you see this file!)
pip3 install -r requirements.txt
```

### Step 4: Verify Setup (Optional)

```bash
# Run the setup checker
python3 setup_check.py
```

### Step 5: Launch Application

```bash
# Run the main application
python3 main.py
```

## 🔑 Default Login Credentials

Based on the database dump, the default user is:

- **Username**: `test_user`
- **Password**: `dummyhash123`

You can also try:

- **Username**: `root` (if you have this user set up)
- **Username**: `customer` (if you have this user set up)

> **Note**: The passwords are stored in the `password_hash` column of the `user` table.
> Check your database for the exact passwords to use.

## 📋 First Steps After Login

### Try the Flashcard Feature

1. Click on the **📇 Flashcards** tab
2. Select "JLPT N5" deck (contains 2 cards)
3. Click **Start Review**
4. Review the cards:
   - Card 1: 犬 (Dog)
   - Card 2: 猫 (Cat)
5. Rate your knowledge (1-5 stars)

### Try the Immersion Materials

1. Click on the **🎬 Immersion Materials** tab
2. As admin (root user), you can:
   - Add new materials (movies, books, podcasts, TV shows)
   - Delete materials
3. As any user, you can:
   - Log materials to your history
   - View your immersion history

## 🔧 Troubleshooting

### "Failed to connect to database"

- Make sure MySQL is running: `mysql.server start`
- Verify the database exists: `mysql -u root -p -e "SHOW DATABASES LIKE 'daigaku'"`
- Check your MySQL root password in the login screen

### "Invalid username or password"

- Check the `user` table in MySQL:
  ```sql
  mysql -u root -p
  USE daigaku;
  SELECT username, password_hash FROM user;
  ```
- Use the exact username and password from the database

### "Module not found" error

```bash
# Make sure you're in the virtual environment
source .venv/bin/activate  # On macOS/Linux

# Reinstall packages
pip3 install -r requirements.txt
```

## 📚 Adding More Content

### Add Users to Database

```sql
mysql -u root -p daigaku

INSERT INTO user (user_id, username, email, password_hash, date_joined, current_level)
VALUES (2, 'customer', 'customer@example.com', 'password123', CURDATE(), 3);
```

### Add More Flashcards

```sql
INSERT INTO flashcard (deck_id, expression, expression_definition, japanese_sentence, english_translation)
VALUES (1, '本', 'Book', '本を読んでいます。', 'I am reading a book.');
```

### Add Immersion Materials

Use the GUI when logged in as `root` user, or via SQL:

```sql
INSERT INTO immersion_material (material_id, title, type, source, length, average_difficulty)
VALUES (1, 'Your Name', 'movie', 'Crunchyroll', 106, 3);
```

## 🎯 Tips for Effective Learning

1. **Review Daily**: The SRS algorithm works best with daily reviews
2. **Be Honest**: Rate cards honestly for optimal scheduling
3. **Log Immersion**: Track everything you watch/read in Japanese
4. **Consistency**: 15 minutes daily beats 2 hours once a week

## 📞 Need Help?

- Check the full README.md for detailed documentation
- Verify setup with: `python3 setup_check.py`
- Check database connection: Login screen shows connection status

---

**Happy Learning! がんばって！(Ganbatte!)**
