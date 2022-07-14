res=$(command -v docker)
length=${#res}

if [[ "$length" -gt 0 ]]; then
    read -p 'Do you want to install this with docker? (Y/n) '
    if [[ "$REPLY" == "Y" ]] || [[ "$REPLY" == "y" ]]; then
        docker-compose --build
        docker-compose up -d
    else
        sudo python3 -m pip install -r requirements.txt
        python3 manage.py migrate
        python3 manage.py runserver
    fi
fi