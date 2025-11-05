#!/usr/bin/env python3
"""
Setup script for Daigaku application.
This script helps with initial database setup and user creation.
"""
import mysql.connector
from mysql.connector import Error


def check_mysql_connection():
    """Check if MySQL is accessible."""
    print("Checking MySQL connection...")
    try:
        connection = mysql.connector.connect(
            unix_socket='/tmp/mysql.sock',
            user='root',
            password='root'
        )
        if connection.is_connected():
            print("✓ MySQL connection successful!")
            connection.close()
            return True
    except Error as e:
        print(f"✗ MySQL connection failed: {e}")
        return False


def check_database_exists():
    """Check if daigaku database exists."""
    print("\nChecking if 'daigaku' database exists...")
    try:
        connection = mysql.connector.connect(
            unix_socket='/tmp/mysql.sock',
            user='root',
            password='root'
        )
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES LIKE 'daigaku'")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if result:
            print("✓ Database 'daigaku' found!")
            return True
        else:
            print("✗ Database 'daigaku' not found.")
            print("  Please import dog.sql using:")
            print("  mysql -u root -p < /path/to/dog.sql")
            return False
    except Error as e:
        print(f"✗ Error checking database: {e}")
        return False


def check_tables():
    """Check if required tables exist."""
    print("\nChecking database tables...")
    required_tables = [
        'user', 'deck', 'flashcard', 'user_card_review',
        'immersion_material', 'user_material_history'
    ]
    
    try:
        connection = mysql.connector.connect(
            unix_socket='/tmp/mysql.sock',
            database='daigaku',
            user='root',
            password='root'
        )
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        cursor.close()
        connection.close()
        
        missing_tables = [t for t in required_tables if t not in tables]
        
        if not missing_tables:
            print(f"✓ All required tables present ({len(tables)} tables)")
            return True
        else:
            print(f"✗ Missing tables: {', '.join(missing_tables)}")
            return False
    except Error as e:
        print(f"✗ Error checking tables: {e}")
        return False


def list_users():
    """List existing users in the database."""
    print("\nExisting users:")
    try:
        connection = mysql.connector.connect(
            unix_socket='/tmp/mysql.sock',
            database='daigaku',
            user='root',
            password='root'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, username, email, current_level FROM user")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        
        if users:
            for user in users:
                print(f"  - {user['username']} (ID: {user['user_id']}, Level: {user['current_level']})")
            return True
        else:
            print("  No users found in database.")
            return False
    except Error as e:
        print(f"✗ Error listing users: {e}")
        return False


def main():
    """Main setup check."""
    print("=" * 50)
    print("Daigaku Setup Verification")
    print("=" * 50)
    
    # Check MySQL connection
    if not check_mysql_connection():
        print("\n⚠️  Please install and start MySQL server.")
        return
    
    # Check database
    if not check_database_exists():
        print("\n⚠️  Please import the database schema first.")
        return
    
    # Check tables
    if not check_tables():
        print("\n⚠️  Database schema incomplete. Please reimport dog.sql.")
        return
    
    # List users
    list_users()
    
    print("\n" + "=" * 50)
    print("✓ Setup verification complete!")
    print("=" * 50)
    print("\nYou can now run the application:")
    print("  python3 main.py")
    print("\nDefault login credentials:")
    print("  Check the 'user' table for usernames and passwords")


if __name__ == "__main__":
    main()
