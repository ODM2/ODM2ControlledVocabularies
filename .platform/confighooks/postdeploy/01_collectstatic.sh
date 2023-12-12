#!/bin/bash

source "$PYTHONPATH/activate" && {

    cd /var/app/current/src/odm2cvs || exit 1;
    echo "Collecting static files as part of AWS auto redeployment of this application due to configuration changes or auto-scaling:";
    python manage.py collectstatic --noinput;
}