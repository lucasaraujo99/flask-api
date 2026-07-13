# Blueprints

> O Blueprint é um conjunto de rotas relacionadas.

Um app Flask tradicional apresenta rotas com o seguinte formato:

```
@app.route('/')
def main():
    return 'Hello World'
```

Porém essa estrutura não é escalável e pode ser tornar desorganizada quando houverem dezenas de rotas.

Assim, os blueprints permitem agrupar rotas relacionadas a mesma entidade, como usuários ou produtos.

```
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users')
def get_user():
    return jsonify({"message":"Esta é a rota de listagem dos usuários"})
```

## Utilizando

Primeiro é preciso importar **Blueprint**

```
from flask import Blueprint
```

Depois é preciso intanciar o módulo de rotas.

```
main_bp = Blueprint('main_bp', __name__)
```

Após é possível criar as rótas do módulo.

```
@main_bp.route('/')
def index():
    return jsonify({"message": "Bem-vindo à API da StyleSync!"})
```

Por fim, é preciso importar e registrar as rotas na instanciação do app

```
from .routes.main import main_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
```
