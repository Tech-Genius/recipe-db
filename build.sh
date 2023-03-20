set -o errexit  # exit on error

pip install -r requirements.txt

# python manage.py collectstatic --no-input
python manage.py migrate
python manage.py sqlflush | python manage.py dbshell
# python manage.py remove_stale_contenttypes
# python manage.py shell 
# from django.contrib.contenttypes.models import ContentType
# ContentType.objects.all().delete()
# exit()
python manage.py loaddata data.json