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

## get_products

```
@main_bp.route('/products', methods=['GET'])
def get_products():

    # pages
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=20, type=int)

    # filters
    category = request.args.get("category", type=str)
    brand = request.args.get("brand", type=str)
    price_min = request.args.get("price_min", type=int)
    price_max = request.args.get("price_max", type=int)
    stock_min = request.args.get("stock_min", type=int)

    # search
    search = request.args.get("search")

    # sorting
    sort = request.args.get("sort")

    query = {}

    if category:
        query["category"] = {
                    "$regex": category,
                    "$options": "i"
                }
    if brand:
        query["brand"] = {
                    "$regex": brand,
                    "$options": "i"
                }

    if price_min or price_max:
        query["price"] = {}

        if price_min is not None:
            query["price"]["$gte"] = price_min

        if price_max is not None:
            query["price"]["$lte"] = price_max

    if stock_min:
        query["stock"] = {"$gte": stock_min}
    
    if search:
        query["$or"] = [
            {
                "name": {
                    "$regex": search,
                    "$options": "i"
                }
            },
            {
                "description": {
                    "$regex": search,
                    "$options": "i"
                }
            }
        ]

    # products_cursor = db.products.find({}) # todos os produtos
    products_cursor = db.products.find(query)

    if sort == "price":
        products_cursor = products_cursor.sort("price", 1)
    elif sort == "-price":
        products_cursor = products_cursor.sort("price", -1)

    products_cursor = products_cursor.skip((page - 1) * limit).limit(limit)


    """
    # lista de produtos com casting de id para string
    products_list = []
    for product in products_cursor:
        # casting do id para string, que originalmete é um ObjectId, que não é json serializable
        product['_id'] = str(product['_id']) 
        products_list.append(product)
    """
    # lista de produtos com casting de id para string (usando a classe criada ProductDBModel() e model_dump() modificado)
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]

    return jsonify(products_list)
```
