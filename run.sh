#!/bin/bash
# Launcher script for Daigaku application

echo "================================"
echo "  Daigaku Language Learning App"
echo "================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found."
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Check if requirements are installed
if ! python -c "import PyQt5" 2>/dev/null; then
    echo "⚠️  Dependencies not installed."
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
fi

# Run the application
echo ""
echo "Starting Daigaku..."
echo ""
python main.py

# Deactivate virtual environment on exit
deactivate
