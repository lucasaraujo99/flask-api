# Requisições HTTP

Uma requisição HTTP é composta por uma URL, um método e, dependendo da operação, parâmetros, cabeçalhos (headers) e corpo (body).

## Estrutura

```
<MÉTODO> <URL>?<query_parameters>
```

Exemplo:

```
GET /products?category=Notebook&page=2
```

---

## Métodos HTTP

| Método | Utilização |
|---------|------------|
| GET | Buscar dados |
| POST | Criar um novo recurso |
| PUT | Atualizar um recurso existente |
| DELETE | Remover um recurso |

---

## Path Parameters

São parâmetros que fazem parte da URL e normalmente identificam um recurso específico.

Exemplo:

```
GET /product/686e5af7fba6327e79b2fb90
```

No Flask:

```
@main_bp.route("/product/<string:product_id>")
```

---

## Query Parameters

São parâmetros opcionais enviados após `?` na URL.

```
GET /products?category=Notebook&brand=Dell
```

Cada parâmetro é separado por `&`.

```
?category=Notebook&brand=Dell&page=2
```

### Parâmetros Disponíveis

| Parâmetro | Tipo | Descrição | Exemplo |
|-----------|-------|-----------|---------|
| `category` | string | Filtra pela categoria. | `?category=Notebook` |
| `brand` | string | Filtra pela marca. | `?brand=Dell` |
| `price_min` | number | Preço mínimo. | `?price_min=3000` |
| `price_max` | number | Preço máximo. | `?price_max=7000` |
| `stock_min` | integer | Estoque mínimo. | `?stock_min=10` |
| `search` | string | Pesquisa por palavras-chave em nome e descrição. | `?search=gamer` |
| `sort` | string | Campo de ordenação. Prefixo `-` indica ordem decrescente. | `?sort=price` ou `?sort=-price` |
| `page` | integer | Página desejada. | `?page=2` |
| `limit` | integer | Quantidade de itens por página. | `?limit=20` |

### Exemplos

Buscar notebooks:

```
GET /products?category=Notebook
```

Buscar notebooks da Dell:

```
GET /products?category=Notebook&brand=Dell
```

Buscar produtos entre R$3000 e R$7000:

```
GET /products?price_min=3000&price_max=7000
```

Pesquisar por "gamer":

```
GET /products?search=gamer
```

Ordenar por preço crescente:

```
GET /products?sort=price
```

Ordenar por preço decrescente:

```
GET /products?sort=-price
```

Paginação:

```
GET /products?page=2&limit=20
```

Combinando filtros:

```
GET /products?category=Notebook&brand=Dell&price_max=7000&sort=-price&page=2&limit=20
```

---

## Request Body

Utilizado principalmente em requisições `POST` e `PUT`.

Normalmente é enviado no formato JSON.

Exemplo:

```
POST /products
```

Body:

```json
{
    "name": "Notebook Gamer Pro X15",
    "description": "Notebook gamer de alta performance.",
    "category": "Notebook",
    "brand": "Dell",
    "price": 9499.99,
    "stock": 50
}
```

---

## Headers

Os headers enviam informações adicionais junto com a requisição.

### Content-Type

Indica o formato do corpo da requisição.

```
Content-Type: application/json
```

### Authorization

Utilizado para enviar o JWT.

```
Authorization: Bearer <token>
```

Exemplo:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

## Upload de Arquivos

Para envio de arquivos, utiliza-se o tipo `multipart/form-data`.

Exemplo:

```
POST /sales/upload
```

No Postman:

- Body
- form-data
- chave: `file`
- tipo: **File**
- selecionar o arquivo `.csv`

---

**OBS:** Uma mesma requisição pode combinar **Path Parameters**, **Query Parameters**, **Headers** e **Body**. Cada um possui uma finalidade diferente.

Exemplo:

```
PUT /product/686e5af7fba6327e79b2fb90?notify=true
```

Headers:

```
Authorization: Bearer <token>
Content-Type: application/json
```

Body:

```json
{
    "price": 7999.99,
    "stock": 25
}
```