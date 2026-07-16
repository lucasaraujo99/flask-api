# Database - MongoDB

Para essa API, iremos usar o MongoDB

## Instalando

```
pip install pymongo
```

## URI

Uniform Resource Identifier (URI) é uma string que identifica um recurso.

ex:
```
MONGO_URI=mongodb://localhost:27017/stylesync
```

Significa algo como: "Conecte ao servidor MongoDB que está neste computador, usando a porta 27017, e utilize o banco chamado stylesync."

## Instanciando DB

```
from pymongo import MongoClient

db = None

client = MongoClient(app.config['MONGO_URI']) # representa a conexão com o servidor MongoDB

db = client.get_default_database() # recupera o database padrão definido no URI
# alternativamente: db = client.get_database("stylesync")
```

**OBS:** MongoClient() é a classe do PyMongo responsável por criar uma conexão com um servidor MongoDB.

## Cursor

Um cursor é um objeto que permite percorrer os resultados da consulta. 

ex:
```
products_cursos = db.products.find({})
```

Ao invés de carregar todos os itens de uma busca em uma lista, find() retorna um cursor, que permite consumir os resultados a medida que for necessário.

