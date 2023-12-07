### flask-db-connection
Create virtual environment and activate it in project folder. (.../**project-folder**/flaskr)

```
$ python3 -m venv .venv
$ . .venv/bin/activate
```

Within the activated environment, use the following command to install Flask
```
$ pip install Flask
```

### Run

```
$ flask --app flaskr init-db
$ flask --app flaskr run --debug
```

Open [http://127.0.0.1:5000/auth/register](http://127.0.0.1:5000/auth/register) in a browser
