# URLs e Methods

Em APIs REST, URLs em conjuntos com os methods são utilizados para designar operações sobre recursos (produtos, usuários, etc).

## Methods

### GET

Permite consultas. Não deve alterar nada.

```
GET /products
```

### POST

Serve para criar um novo recurso.

```
POST /products
```

Corpo da requisição.

```
{
    "nome": "Mouse",
    "preco": 120
}
```

Ao final da requisição, vai haver uma inserção a mais no servidor.

### PUT

Serve para substituir ou atualizar um recurso que já existe.

```
PUT /product/3
```

**OBS:** ao utilizar o método put, você sabe qual recurso você quer alterar.

### DELETE

Remove um recurso.

```
DELETE /product/3
```

### Idempotência

Um método é idempotente quando repetir a mesma requisição várias vezes produz o mesmo estado final.

GET, PUT e DELETE são idempotentes. Já POST não é, pois mesmo inserindo os mesmos dados, servidor irá instanciar objetos diferentes, com ids diferentes.

## Mesma URL e métodos diferentes

No protocolo HTTP, tanto a URL, quanto o método HTTP são relevantes. Uma mesma URL representa um mesmo recurso, enquanto métodos diferentes representam operaões diferentes sobre esse recurso.

Retorna a lista de produtos:
```
GET /products
```

Cria um novo produto:
```
POST /products
```

Retorna o produto de id 15:
```
GET /products/15
```

Atualiza o produto de id 15:
```
PUT /products/15
```



