# Decorators

Decorators são funções que adicionam algum comportamento antes ou depois da execução de outra função. Para isso, uma função original, cujo o comportamento se quer alterar, é passada como argumento para outra função, o **decorator**, que retornam uma nova função.

São muito utilizados para reutilizar funcionalidades sem modificar o código da função decorada.

## Sintaxe

```
@decorator
def minha_funcao():
    ...
```

É equivalente a:

```
def minha_funcao():
    ...

minha_funcao = decorator(minha_funcao)
```

## Criando um Decorator

```
def meu_decorator(func):

    def wrapper():
        print("Antes")

        func()

        print("Depois")

    return wrapper
```

## Utilizando

```
@meu_decorator
def ola():
    print("Olá!")
```

Resultado:

```
Antes
Olá!
Depois
```

## Decorators com Argumentos

Quando a função decorada recebe parâmetros, o decorator também deve recebê-los.

```
def meu_decorator(func):

    def wrapper(*args, **kwargs):

        print("Antes")

        resultado = func(*args, **kwargs)

        print("Depois")

        return resultado

    return wrapper
```

## @wraps

```
from functools import wraps
```

```
@wraps(func)
def wrapper(*args, **kwargs):
    ...
```

O @wraps copia informações da função original (nome, documentação, etc.) para a função wrapper.

Sem ele, a função decorada passa a ser identificada como wrapper.

## Exemplo no Flask

```
@token_required
def get_products(token):
    ...
```

Antes de executar `get_products()`, o decorator `token_required` valida o JWT enviado na requisição. Caso o token seja válido, a função original é executada.

**OBS:** Decorators são muito utilizados em frameworks como Flask, Django e FastAPI para implementar autenticação, autorização, cache, logs e validações sem repetir código.

## Estrutura de um Decorator

```
def decorator(func):

    def wrapper(*args, **kwargs):

        ...

        return func(*args, **kwargs)

    return wrapper
```

- `func` é a função que será decorada.
- `wrapper` é a nova função que será executada.
- `return wrapper` substitui a função original pela nova função.

**OBS:** a função original não é modificada. O decorator cria uma nova função que envolve ("embrulha") a função original.