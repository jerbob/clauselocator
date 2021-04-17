#!/usr/bin/env sh

echo -n "Waiting for postgres... "

while ! nc -z db 5432
do
  # Wait for postgres port to open
  sleep 0.1
done
echo "Done."

python ./manage.py migrate --no-input
python ./manage.py collectstatic --no-input
