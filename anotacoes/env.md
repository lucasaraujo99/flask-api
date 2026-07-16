# .env

Guarda configurações e informações sensíveis fora do código-fonte

ex:
```
MONGO_URI=mongodb://localhost:27017/database
```

## Instalando

```
pip install python-dotenv
```

## Acessando variáveis

```
import os # permite trabalhar com o sistema operacional
from dotenv import load_dotenv

load_dotenv() # responsável por ler o arquivo .env e carregar as variáveis definidas nele

mongo_uri = os.getenv("MONGO_URI") # recupera a variável criada no arquivo .env
```
