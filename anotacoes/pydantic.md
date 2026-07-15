# Pydantic

O Pydantic é uma biblioteca para criar modelos de dados com validação automática.

## Instalando

```
pip install pydantic
```

## Importando

```
from pydantic import BaseModel
```

## Declarando Classes

Primeiro a classe precisa herdar BaseModel.

```
class Product(BaseModel):

    name: str
    price: float
    stock: int
```

Depois é possível definir o tipo de cada atributo.

**OBS:** quem cria o construtor é a própria classe BaseModel.

## Instanciando Objetos

```
Product(
    name="Notebook",
    price=5000,
    stock=10
)
```

**OBS:** o pydantic aplica **coerção de tipos**. Assim, a string "19,99" pode virar um inteiro pra se adequar a validação