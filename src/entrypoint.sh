#!/usr/bin/env sh

echo -n "Waiting for postgres... "

while ! nc -z db 5432
do
  # Wait for postgres port to open
  sleep 0.1
done
echo "Done."

python src/manage.py migrate --no-input
python src/manage.py collectstatic --no-input

exec "$@"
