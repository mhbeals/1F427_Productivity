# heroku create prod-cw18
# git push heroku master

# heroku logs --tail
git push heroku master

#heroku ps:scale web=1
heroku restart
heroku open

# load fixtures
heroku run python manage.py makemigrations    
heroku run python manage.py migrate
heroku run python manage.py loaddata core/fixtures/units.yaml 
heroku run python manage.py loaddata core/fixtures/emoji.json 
heroku run python manage.py loaddata core/fixtures/tasks.yaml 