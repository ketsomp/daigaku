#!/usr/bin/env python3
"""
Script to set up user login credentials for Daigaku application.
Sets root password to "root" and customer password to "customer"
"""
import mysql.connector
from mysql.connector import Error


def setup_users():
    """Set up user credentials in the database."""
    try:
        connection = mysql.connector.connect(
            unix_socket='/tmp/mysql.sock',
            database='daigaku',
            user='root',
            password='root'
        )
        cursor = connection.cursor()
        
        print("=" * 60)
        print("Setting up user credentials...")
        print("=" * 60)
        
        # Update or insert root user
        cursor.execute("""
            INSERT INTO user (user_id, username, email, password_hash, date_joined, current_level, vocabulary_learnt)
            VALUES (1, 'root', 'root@daigaku.com', 'rootpass', CURDATE(), 5, 0)
            ON DUPLICATE KEY UPDATE 
                password_hash = 'rootpass',
                username = 'root',
                email = 'root@daigaku.com'
        """)
        print("✓ Root user configured (username: root, password: rootpass)")
        
        # Update or insert customer user
        cursor.execute("""
            INSERT INTO user (user_id, username, email, password_hash, date_joined, current_level, vocabulary_learnt)
            VALUES (2, 'customer', 'customer@daigaku.com', 'customer1', CURDATE(), 3, 0)
            ON DUPLICATE KEY UPDATE 
                password_hash = 'customer1',
                username = 'customer',
                email = 'customer@daigaku.com'
        """)
        print("✓ Customer user configured (username: customer, password: customer1)")
        
        connection.commit()
        
        # Verify the changes
        print("\n" + "=" * 60)
        print("Current users in database:")
        print("=" * 60)
        cursor.execute("SELECT user_id, username, password_hash, email FROM user")
        users = cursor.fetchall()
        
        for user in users:
            print(f"\n👤 Username: {user[1]}")
            print(f"🔑 Password: {user[2]}")
            print(f"📧 Email: {user[3]}")
            print("-" * 60)
        
        cursor.close()
        connection.close()
        
        print("\n✅ User setup complete!")
        print("\nYou can now login with:")
        print("  • Username: root     | Password: rootpass")
        print("  • Username: customer | Password: customer1")
        
    except Error as e:
        print(f"❌ Error: {e}")
        print("\nMake sure:")
        print("1. MySQL is running")
        print("2. Database 'daigaku' exists")


if __name__ == "__main__":
    setup_users()
