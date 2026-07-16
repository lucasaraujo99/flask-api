import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")

"""
# Config

Ao criar a classe Config, podemos acessar diretamente:

```
Config.MONGO_URI
```

Ao invés de precisar antes instanciar a configuração, como em:

```
config = Config()

print(config.MONGO_URI)
```

## No Flask

Na instaciação do app Flask, chamamos a configuração

```
app = Flask(__name__)
app.config.from_object("config.Config")
```

"""