#!/bin/bash
# Unified collectstatic script with dynamic virtualenv
# Works for beta and prod environments
# Prints detailed messages on failures

set -euo pipefail

echo "Starting collectstatic script..."

# Resolve virtual environment dynamically
VENV_DIR=$(ls -d /var/app/venv/* | head -n 1)
VENV_ACTIVATE="$VENV_DIR/bin/activate"

if ! source "$VENV_ACTIVATE"; then
    echo "ERROR: Failed to activate virtual environment at $VENV_ACTIVATE"
    exit 1
else
    echo "Virtual environment activated successfully."
fi

# Change directory to Django project
PROJECT_DIR="/var/app/current/src/odm2cvs"
if ! cd "$PROJECT_DIR"; then
    echo "ERROR: Failed to cd into project directory $PROJECT_DIR"
    exit 1
else
    echo "Changed directory to $PROJECT_DIR"
fi

# Run collectstatic on leader or single-instance node
if [[ "${EB_IS_COMMAND_LEADER:-}" == "true" ]] || [[ -z "${EB_IS_COMMAND_LEADER:-}" ]]; then
    echo "Collecting static files..."
    if ! python manage.py collectstatic --noinput; then
        echo "ERROR: collectstatic command failed!"
        exit 1
    else
        echo "Static files collected successfully."
    fi
else
    echo "Skipping collectstatic on non-leader node."
fi

echo "collectstatic script finished."
