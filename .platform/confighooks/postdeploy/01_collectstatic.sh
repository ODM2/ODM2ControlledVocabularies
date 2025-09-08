#!/bin/bash
# Manual collectstatic trigger via env update
set -euo pipefail

echo "Manual collectstatic trigger (confighooks/postdeploy)..."

# Resolve virtual environment
VENV_DIR=$(ls -d /var/app/venv/* | head -n 1)
VENV_ACTIVATE="$VENV_DIR/bin/activate"
if ! source "$VENV_ACTIVATE"; then
    echo "ERROR: Failed to activate virtual environment at $VENV_ACTIVATE"
    exit 1
fi
echo "Virtual environment activated."

# Change to Django project
PROJECT_DIR="/var/app/current/src/odm2cvs"
if ! cd "$PROJECT_DIR"; then
    echo "ERROR: Failed to cd into $PROJECT_DIR"
    exit 1
fi
echo "Changed directory to $PROJECT_DIR"

# Always run on single-instance / leader node
echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Static files collected successfully."
