# Rotas da API

## Login 

O sistema deve permitir que um usuário se autentique para obter um token

### Request

A requisição é feita através de um endereço, um método http e um corpo com informações.

Endereço:
```
POST http://127.0.0.1:5000/login
```

Corpo:
```
{
	"username": "Lucas",
    "password": "senha"
}
```

### Rota

```
@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json() # o método request permite recuperar as informações passadas na requisição
        user_data = LoginPayload(**raw_data) # pydantic: a instanciação permite a validação dos dados
    except ValidationError as e: # 
        return jsonify({"message": e.errors()}), 400 # erro do cliente
    except Exception as e:
        jsonify({"message": "Erro durante a requisição."}), 500 # erro do servidor
    return jsonify({"message":f"Realizar o login do usuário {user_data.model_dump_json()}"}), 200 # sucesso. OBS: é opcional no Flask
```

**OBS:** o operador ** desacopla o dicionário em argumentos de palavras-chave atribuídos automaticamente aos atributos de classe.

**OBS:** try ... except permite ao programa executar o except, ao invés de encerrar o programa, quando acontece uma exceção

**OBS:** ValidationError é uma exceção criada pelo Pydantic.
- A função errors() mostra dados do erro que aconteceu

**OBS:** Exception é um objeto que representa um erro ocorrido durante a execução do programa.
- ValueError
- ZeroDivisionError 

**OBS:** model_dump_json() transforam um objeto em uma string no formato json
