-- Update user passwords for Daigaku application
-- This script sets the passwords for root and customer users

-- Update or insert root user (password must be at least 8 characters)
INSERT INTO user (user_id, username, email, password_hash, date_joined, current_level, vocabulary_learnt)
VALUES (1, 'root', 'root@daigaku.com', 'rootpass', CURDATE(), 5, 0)
ON DUPLICATE KEY UPDATE 
    password_hash = 'rootpass',
    username = 'root',
    email = 'root@daigaku.com';

-- Update or insert customer user (password must be at least 8 characters)
INSERT INTO user (user_id, username, email, password_hash, date_joined, current_level, vocabulary_learnt)
VALUES (2, 'customer', 'customer@daigaku.com', 'customer1', CURDATE(), 3, 0)
ON DUPLICATE KEY UPDATE 
    password_hash = 'customer1',
    username = 'customer',
    email = 'customer@daigaku.com';

-- Verify the changes
SELECT user_id, username, password_hash, email FROM user;
