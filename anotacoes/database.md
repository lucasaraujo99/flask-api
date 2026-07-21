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

## Operações CRUD

### Buscar Todos

```
products_cursor = db.products.find({})
```

Retorna um cursor contendo todos os documentos da coleção.

Também é possível utilizar filtros.

```
db.products.find({"category": "Notebook"})
```

---

### Buscar Um Documento

```
product = db.products.find_one({"_id": ObjectId(product_id)})
```

Retorna o primeiro documento que satisfaz o filtro ou `None`, caso não exista.

---

### Inserir Um Documento

```
db.products.insert_one(
    {
        "name": "Notebook",
        "price": 5000,
        "stock": 10
    }
)
```

Retorna um objeto contendo o `_id` do documento criado.

---

### Inserir Vários Documentos

```
db.products.insert_many(products_list)
```

`products_list` deve ser uma lista de dicionários.

```
[
    {
        "name": "...",
        "price": ...
    },
    {
        "name": "...",
        "price": ...
    }
]
```

---

### Atualizar Um Documento

```
db.products.update_one(
    {"_id": ObjectId(product_id)},
    {
        "$set": {
            "price": 4500
        }
    }
)
```

`$set` atualiza apenas os campos informados.

---

### Atualizar Vários Documentos

```
db.products.update_many(
    {"category": "Notebook"},
    {
        "$set": {
            "stock": 0
        }
    }
)
```

Atualiza todos os documentos que satisfazem o filtro.

---

### Remover Um Documento

```
db.products.delete_one(
    {"_id": ObjectId(product_id)}
)
```

---

### Remover Vários Documentos

```
db.products.delete_many(
    {"stock": 0}
)
```

Remove todos os documentos que satisfazem o filtro.

**OBS:** Os métodos `find()`, `find_one()`, `insert_one()`, `insert_many()`, `update_one()`, `update_many()`, `delete_one()` e `delete_many()` pertencem ao objeto da coleção (`db.products`). Basta substituir `products` pelo nome da coleção desejada.

