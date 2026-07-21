# Flask API

Projeto de API em Flask.

**Palavras-chave:** API, Flask, blueprints, JWT, decorators, MongoDB, Pydantic, json, http, filters, sorting e pagination

## Objetivos

- Desenvolvimento de API com Flask
- Organização das rotas atráves de **blueprints**
- Implementação de autenticação com **JWT**, sem necessidade de guarda estado da seção (stateless)
- Utilização de **decorators**, para implementar a necessidade de tokens de autenticação para usar as rotas
- Integração com o MongoDB, realizando operações de leitura, escrita, atualização e exclusão de dados
- Modelagem e validação de dados com **Pydantic**
- Retorno de rotas no formato **json** e **status http**
- Criação de **http requests** com filters, sorting e pagination para testar as rotas criadas

## Endpoints da API

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| POST | `/login` | Autenticação |
| GET | `/products` | Lista produtos |
| POST | `/products` | Cria um produto |
| GET | `/product/{id}` | Busca um produto |
| PUT | `/product/{id}` | Atualiza um produto |
| DELETE | `/product/{id}` | Remove um produto |
| POST | `/products/upload` | Importa produtos via CSV |
| POST | `/sales/upload` | Importa vendas via CSV |

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

### .env

.env é o arquivo de variáveis de ambiente. Guarda dados como URI do MongoDB e SECRET_KEY de criptografia.

Opções:
1. Criar um arquivo .env baseado no arquivo .env.example
2. Renomear .env.example para .env e alterar os valores das variáveis

### Rodar
```
python app.py
```

## Documentação

A documentação completa da API está disponível em:

```
docs/api.md
```

## Estrutura do Projeto

```
flask-api/
├── app/
|   ├── models/
|   ├── routes/
|   |   └── main.py
|   └── __init__.py
├── csv/
├── docs/
├── exemplos/
├── .env
├── config.py
├── run.py
└── ...
```

anotacoes/ → material de consulta

app/ → contém o código fonte da aplicação (instanciação, routes, etc)

`__init__.py` → cria a aplicação (instanciação do app Flask e importação de rotas)

models/ → modelos de dados utilizando o Pydantic (organizando as definições e estruturas de dados da lógica de negócio)

routes/ → diretório de módulos de rotas (Blueprints)

csv/ → arquivos csv usados para inserção de vários itens no banco de dados com rotas de upload (upload_products, upload_sales)

docs/ → documentação sobre rotas da api e como criar requisições http para essas rotas

exemplos/ → exemplos de aplicação web (uma com python puro com front-end e back-end e outra em Flask básico)

.env → contém as variáveis de ambiente (URI, SECRET_KEY, etc)

run.py → arquivo responsável por rodar a aplicação