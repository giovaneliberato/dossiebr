Tekton Template App
==================

This is a simple app I use to quick start any project using [Tekton](https://github.com/renzon/tekton-micro) + Google App Engine

#### Requirements
- [virtualenvwrapper](virtualenvwrapper.readthedocs.org)

### Usage
##### Clone this repo
```shell
$ git clone git@github.com:giovaneliberato/tekton-templateapp.git {{ YOUR_APP_NAME }}
```

##### Go to your project folder and create a virtual env using virtualenvwrapper

```shell
$ cd {{ YOUR_APP_NAME }}
$ mkvirtualenv {{ YOUR_APP_NAME }}
```

##### Run the setup script
```shell
$ ./venv/setup_venv.sh
```

##### You're ready to go! Run server
```shell
$ ./runlocal.sh
```
