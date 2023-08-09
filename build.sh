#!usr/bin/env/ bash
# exit on error

set -o errexit
pip install --upgrade pip
pip install -r requirements.txt

python manage.py collecttstatic --no-input
python manage.py migrate