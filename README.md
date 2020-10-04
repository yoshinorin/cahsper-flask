# Cahsper - Flask (experimental)

_**NOTE: Sandbox implementation for learning python and Flask with Cahsper**_

> _Original Cahsper [is here](https://github.com/YoshinoriN/cahsper)._

## Install pyenv

> [pyenv](https://github.com/pyenv/pyenv)

```sh
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
// bash
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
$ exec "$SHELL" -l

$ pyenv --version
pyenv 1.2.20-7-gdd62b0d1
```

## switch python version

```sh
$ pyenv local 3.8.6
$ pyenv versions
  system
* 3.8.6 (set by cahsper-flask/.python-version)
```

## Install pipenv

DO NOT USE `apt-get install pipenv`

```sh
$ pip3 install pipenv

// upgrade
$ pip3 install --user --upgrade pipenv
```

## swhich pipenv python version

```sh
$ pipenv --python 3.8.6
```

## Install dependencies

> [Flask](https://flask.palletsprojects.com/en/1.1.x/)
> [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

```sh
$ pipenv install flask flask-sqlalchemy
```

## Settings

1. copy `.env.example` and rename it to `.env`
2. change settings in `.env`

## Run application

```
$ sh run.sh

 * Serving Flask app "cahsper" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

> http://127.0.0.1:5000

## Test

```
$ pytest
```
