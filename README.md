Dossiê BR
==================

O doss.ie é uma plataforma que te ajuda a fiscalizar as promessas e resultados do seu candidato. Com ele você pode arquivar e gerenciar as notícias de um determinado candidato e receber periodicamente um resumo destas notícias por email.

#### Tech Stack
- [Google App Engine](https://cloud.google.com/appengine/docs)
- Python
- AngularJS
- [Tekton](https://github.com/renzon/tekton-micro)

#### Requirements
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org)

### Instalação
##### Clonar repositório
```shell
$ git clone git@github.com:giovaneliberato/dossiebr.git
```

##### Vá para o diretório do projeto e crie um virtual environment

```shell
$ cd dossiebr
$ mkvirtualenv dossiebr
```

##### Script de setup
```shell
$ ./venv/setup_venv.sh
```

##### Rodar servidor local
```shell
$ ./runlocal.sh
```
