# Número por Extenso
3 formas de rodar a aplicação.
1. **Heroku**
2. **Docker**
3. **Virtualenv**

## Usando heroku
* Link do projeto https://num-extenso.herokuapp.com/140/ é só mudar o final endpoint (/140/)

## Usando Docker
* Clonar o projeto dentro de alguma pasta do computador.
* git clone https://github.com/anthonylopez15/numero_extenso.git
* Abrir o cmd dentro da pasta do projeto e dar os seguintes comandos:
```
docker-compose build
docker-compose up
```
* Abrir no navegador http://<ip_virtualbox>:8000/{aqui_o_numero_desejado}/
## Usando Virtualenv
* Clonar o projeto - git clone https://github.com/anthonylopez15/numero_extenso.git
```
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
http://localhost:8000/{aqui_o_numero_desejado}/
```
