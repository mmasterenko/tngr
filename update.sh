git pull
yes yes | ./venv/bin/python ./manage.py collectstatic
kill -HUP `pgrep gunicorn`

