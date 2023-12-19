#!/bin/bash

source "$PYTHONPATH/activate" && {

    if [[ $EB_IS_COMMAND_LEADER == "true" ]];
    then
        cd /var/app/current/src/odm2cvs || exit 1;
        echo "Collecting static files:";
        python manage.py collectstatic --noinput;
    else
        echo "Skipping static collection on non-leader node.";
    fi

}