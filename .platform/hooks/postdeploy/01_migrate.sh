#!/bin/bash
# Robust EB migrate script with dynamic virtualenv
# Works for beta and prod environments
# Prints detailed error messages

set -euo pipefail

echo "Starting Django migrate script..."

# Resolve virtual environment dynamically
VENV_DIR=$(ls -d /var/app/venv/* | head -n 1)
VENV_ACTIVATE="$VENV_DIR/bin/activate"

if ! source "$VENV_ACTIVATE"; then
    echo "ERROR: Failed to activate virtual environment at $VENV_ACTIVATE"
    exit 1
else
    echo "Virtual environment activated successfully."
fi

# Change to Django project directory
PROJECT_DIR="/var/app/current/src/odm2cvs"
if ! cd "$PROJECT_DIR"; then
    echo "ERROR: Failed to cd into project directory $PROJECT_DIR"
    exit 1
else
    echo "Changed directory to $PROJECT_DIR"
fi

# Run migrations on leader or single-instance node
if [[ "${EB_IS_COMMAND_LEADER:-}" == "true" ]] || [[ -z "${EB_IS_COMMAND_LEADER:-}" ]]; then
    echo "Listing migrations before migrate:"
    python manage.py showmigrations || echo "WARNING: Failed to list migrations (pre-migrate)"

    echo "Running migrate command..."
    if ! python manage.py migrate --noinput; then
        echo "ERROR: Django migrate command failed!"
        exit 1
    else
        echo "Django migrate completed successfully."
    fi

    echo "Listing migrations after migrate:"
    python manage.py showmigrations || echo "WARNING: Failed to list migrations (post-migrate)"
else
    echo "Skipping migrations on non-leader node."
fi

echo "Django migrate script finished."
