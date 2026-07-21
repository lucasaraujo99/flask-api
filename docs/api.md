# API Documentation

## Base URL

```
http://localhost:5000
```
ou
```
http://127.0.0.1:5000
```

---

# Authentication

## Login

Autentica um usuário e retorna um JWT.

### Endpoint

```
POST /login
```

### Request Body

```json
{
    "username": "admin",
    "password": "123"
}
```

### Success Response (200)

```json
{
    "access_token": "<jwt_token>"
}
```

### Error Response

**401 Unauthorized**

```json
{
    "message": "Credenciais inválidas!"
}
```

---

# Products

## List Products

Retorna uma lista de produtos.

### Endpoint

```
GET /products
```

### Query Parameters

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| category | string | Filtra pela categoria. |
| brand | string | Filtra pela marca. |
| price_min | number | Preço mínimo. |
| price_max | number | Preço máximo. |
| stock_min | integer | Estoque mínimo. |
| search | string | Pesquisa por nome e descrição. |
| sort | string | Campo de ordenação (`price` ou `-price`). |
| page | integer | Página. |
| limit | integer | Quantidade de itens por página. |

### Example

```
GET /products?category=Notebook&brand=Dell&sort=-price&page=1&limit=10
```

---

## Get Product by ID

Retorna um produto pelo ID.

### Endpoint

```
GET /product/{product_id}
```

### Path Parameters

| Nome | Tipo |
|------|------|
| product_id | string |

### Example

```
GET /product/686e5af7fba6327e79b2fb90
```

---

## Create Product

Cria um novo produto.

### Endpoint

```
POST /products
```

### Authentication

Bearer Token obrigatório.

### Headers

```
Authorization: Bearer <jwt_token>
```

### Request Body

```json
{
    "name": "Notebook Gamer",
    "description": "Notebook gamer de alta performance.",
    "category": "Notebook",
    "brand": "Dell",
    "price": 9499.99,
    "stock": 50
}
```

### Success Response

**201 Created**

---

## Update Product

Atualiza um produto existente.

### Endpoint

```
PUT /product/{product_id}
```

### Authentication

Bearer Token obrigatório.

### Headers

```
Authorization: Bearer <jwt_token>
```

### Path Parameters

| Nome | Tipo |
|------|------|
| product_id | string |

### Request Body

Todos os campos são opcionais.

```json
{
    "price": 8999.99,
    "stock": 30
}
```

### Success Response

**200 OK**

---

## Delete Product

Remove um produto.

### Endpoint

```
DELETE /product/{product_id}
```

### Authentication

Bearer Token obrigatório.

### Headers

```
Authorization: Bearer <jwt_token>
```

### Path Parameters

| Nome | Tipo |
|------|------|
| product_id | string |

### Success Response

**200 OK**

---

## Upload Products

Importa produtos através de um arquivo CSV.

### Endpoint

```
POST /products/upload
```

### Authentication

Bearer Token obrigatório.

### Headers

```
Authorization: Bearer <jwt_token>
```

### Body

```
multipart/form-data
```

Campo:

| Nome | Tipo |
|------|------|
| file | CSV |

---

# Sales

## Upload Sales

Importa vendas através de um arquivo CSV.

### Endpoint

```
POST /sales/upload
```

### Authentication

Bearer Token obrigatório.

### Headers

```
Authorization: Bearer <jwt_token>
```

### Body

```
multipart/form-data
```

Campo:

| Nome | Tipo |
|------|------|
| file | CSV |

### Success Response

```json
{
    "message": "Upload processado com sucesso.",
    "vendas_importadas": 100,
    "erros_encontrados": []
}
```