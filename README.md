#### Heroku setup:

```
heroku create
heroku addons:create auth0:free -a APP_NAME
```

#### Generate .env:
```
heroku config -s -a APP_NAME | grep 'AUTH0_CLIENT_ID\|AUTH0_CLIENT_SECRET\|AUTH0_DOMAIN' | tee -a .env
echo "FLASK_ENV=development" >> .env
```

#### Auth0 setup:
1. Go to Auth0 dashboard for your current Heroku application.
2. Select Applications in the left sidebar and select Default App.
3. Add the URL of your Heorku application to Allowed Logout URLs. If you want to run the application locally, you need to add "http://localhost:5000" to Allowed Logout URLs as well.
4. More details about Allowed Logout URLs can be found [here][auth0-allowed-logout-urls]


#### Install dependencies and run app:
```
pipenv install
pipenv shell
heroku local dev
```

#### Debugging:
1. You can use `heroku logs --tail` to check the log for your Heroku application.
2. You can go to Auth0 dashboard and select 'logs' in the left sidebar for Auth0 log.

#### Some materials that may help:

https://auth0.com/docs/quickstart/webapp/python/01-login \
https://auth0.com/docs/logout/redirect-users-after-logout \
https://trstringer.com/logging-flask-gunicorn-the-manageable-way/ \
https://stackoverflow.com/questions/61922045/mismatchingstateerror-mismatching-state-csrf-warning-state-not-equal-in-reque

[auth0-allowed-logout-urls]: https://auth0.com/docs/quickstart/webapp/python/01-login#configure-logout-urls

Reference: https://github.com/umn-5117-f18/in-class-10-03
