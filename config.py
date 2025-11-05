"""
Configuration management for Daigaku application.
"""
import configparser
import os


class Config:
    """Application configuration manager."""
    
    def __init__(self, config_file='config.ini'):
        """Initialize configuration."""
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        
        # Set defaults
        self.config['database'] = {
            'host': 'localhost',
            'database': 'daigaku',
            'user': 'root',
            'password': '',
            'unix_socket': '/tmp/mysql.sock'
        }
        self.config['application'] = {
            'default_users': 'root, customer'
        }
        
        # Load from file if exists
        if os.path.exists(config_file):
            self.config.read(config_file)
    
    def get_db_config(self):
        """Get database configuration."""
        return {
            'host': self.config['database']['host'],
            'database': self.config['database']['database'],
            'user': self.config['database']['user'],
            'password': self.config['database']['password'],
            'unix_socket': self.config['database'].get('unix_socket', '/tmp/mysql.sock')
        }
    
    def get_default_users(self):
        """Get default user list."""
        users_str = self.config['application']['default_users']
        return [u.strip() for u in users_str.split(',')]
