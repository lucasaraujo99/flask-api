# JWT (JSON Web Token)

JWT (JSON Web Token) é um padrão para autenticação e troca segura de informações entre cliente e servidor.

Após o login, o servidor gera um token e o envia ao cliente. Nas próximas requisições, o cliente envia esse token para comprovar sua identidade.

## Instalando

```
pip install PyJWT
```

## Importando

```
import jwt
```

## Gerando um Token

```
from datetime import datetime, timedelta, timezone

token = jwt.encode(
    {
        "user_id": "admin",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    },
    SECRET_KEY,
    algorithm="HS256"
)
```

- `user_id`: informações (payload) que serão armazenadas no token.
- `exp`: data e hora de expiração do token.
- `SECRET_KEY`: chave utilizada para assinar o token.
- `algorithm`: algoritmo de criptografia utilizado na assinatura.

## Validando um Token

```
data = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)
```

Se o token for válido, `data` conterá o payload.

Exemplo:

```
{
    "user_id": "admin",
    "exp": ...
}
```

## Tratando Erros

```
try:
    data = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

except jwt.ExpiredSignatureError:
    ...

except jwt.InvalidTokenError:
    ...
```

- `ExpiredSignatureError`: token expirado.
- `InvalidTokenError`: token inválido ou alterado.

## Enviando o Token

O token normalmente é enviado no cabeçalho HTTP Authorization.

```
Authorization: Bearer <token>
```

No Flask:

```
token = request.headers["Authorization"]
```

## Obtendo Apenas o Token

```
auth_header = request.headers["Authorization"]

token = auth_header.split(" ")[1]
```

Exemplo:

```
Bearer eyJhbGciOiJIUzI1NiIs...
```

↓

```
eyJhbGciOiJIUzI1NiIs...
```

## Utilizando com Decorators

```
@token_required
def get_products(token):
    ...
```

O decorator valida o token antes da execução da rota.

Se o token for inválido, a requisição é interrompida e um erro HTTP 401 é retornado.

**OBS:** O JWT não armazena sessão no servidor. Toda a informação necessária para validar o usuário está contida no próprio token, que é assinado digitalmente utilizando a `SECRET_KEY`.

**OBS:** O conteúdo do JWT pode ser lido por qualquer pessoa que possua o token. Informações sensíveis não devem ser armazenadas no payload.