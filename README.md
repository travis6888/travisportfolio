To set it up locally:

1. make a virtualenv
2. pip install -r requirements.txt
3. configure PyCharm accordingly (you know)
4. export AWS_ACCESS_KEY_ID="yourkeyidgoeshere"
5. export AWS_SECRET_ACCESS_KEY="yoursecretkeygoeshere"
6. python manage.py syncdb


To deploy to heroku:

1. python manage.py collectstatic
2. git push heroku master
3. heroku run python manage.py syncdb
4. heroku run python manage.py migrate
5. heroku ps:scale web=1
