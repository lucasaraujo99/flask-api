# Flask API

Projeto de API em Flask.

## Objetivos

- Desenvolva APIs e aplicações web com Flask, estruturando rotas e integrando boas práticas de projeto.
- Implemente autenticação segura com JWT, protegendo rotas e garantindo autorização adequada.
- Integre o MongoDB à sua aplicação, realizando operações de leitura, escrita, atualização e exclusão de dados.
- Valide e modele dados com Pydantic, garantindo consistência e segurança nas entradas da API.
- Automatize a qualidade do código com pytest, criando testes unitários que aumentam a confiabilidade da aplicação.
- Aplique práticas modernas de DevOps, utilizando Docker, Kubernetes e Redis para escalabilidade e performance.
- Organize seus projetos com boas práticas de arquitetura, preparando aplicações Python para manutenção e evolução contínua.

## Inicialização e Execução do Projeto

### Criar pasta venv
- linux: 
```
python3 -m venv venv 
```

- windows: 
```
py -3 -m venv .venv
```

### Ativa ambiente virtual
- linux: 
```
source /venv/bin/activate /
```

- windows: 
```
.venv\Scripts\activate
```

### Instalar requerimentos
``` 
pip install -r requirements.txt
```

**OBS:** para atualizar o requirements é possível usar **pip freeze**
```
pip freeze > requirements.txt
```

### Rodar
```
python app.py
```

## Estrutura do Projeto

```
flask-api/
├── app/
|   ├── models/
|   ├── routes/
|   |   └── main.py
|   └── __init__.py
├── app_exemplo/
├── .env
├── config.py
├── run.py
└── ...
```

anotacoes/ → material de consulta

app/ → contém o código fonte da aplicação (instanciação, routes, etc)

__init__.py → cria a aplicação (instanciação do app Flask e importação de rotas)

models/ → modelos de dados utilizando o Pydantic (organizando as definições e estruturas de dados da lógica de negócio)

routes/ → diretório de módulos de rotas (Blueprints)

app_exemplo/ → exemplo de aplicação web em python puro com front-end e back-end

.env → contém as variáveis de ambiente (URI)

run.py → arquivo responsável por rodar a aplicação