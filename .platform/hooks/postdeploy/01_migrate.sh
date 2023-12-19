#!/bin/bash

source "$PYTHONPATH/activate" && {

    if [[ $EB_IS_COMMAND_LEADER == "true" ]];
    then
        cd /var/app/current/src/odm2cvs || exit 1;
        echo "Listing migrations before running migrate command:";
        python manage.py showmigrations;
        echo "Running migrate command:";
        python manage.py migrate --noinput;
        echo "Listing migrations after running migrate command:";
        python manage.py showmigrations;
    else
        echo "Skipping migrations on non-leader node.";
    fi

}