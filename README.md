Auth0 setup:

> heroku addons:create auth0:free -a APP_NAME
> heroku config -s -a APP_NAME | grep 'AUTH0_CLIENT_ID\|AUTH0_CLIENT_SECRET\|AUTH0_DOMAIN' | tee -a .env

psycopg2 (for postgresql)
authlib (for auth0)

> heroku config -a APP_NAME -s > .env
> echo "FLASK_ENV=development" >> .env
(Set development/debug env to enable hot-reloading)

cat schema.sql | heroku pg:psql --app APP_NAME

https://trstringer.com/logging-flask-gunicorn-the-manageable-way/



If it displays Oops! Something went wrong! 
Auth0 dashboard - logs - check the error messages
Auth0 dashboard - Applications - Select the app you are using(ClientID) - Add your URL to allowed callback/logout URLs

https://auth0.com/docs/quickstart/webapp/python/01-login#configure-logout-urls
https://auth0.com/docs/logout/redirect-users-after-logout
