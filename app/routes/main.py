from flask import Blueprint, jsonify, request
from app.models.user import LoginPayload
from pydantic import ValidationError
from app import db
from bson import ObjectId

main_bp = Blueprint('main_bp', __name__)

# RF: O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data) # a instanciação permite a validação dos dados
        # o operador ** desacopla o dicionário em argumentos de palavras-chave atribuídos automaticamente aos atributos de classe.
    except ValidationError as e:
        return jsonify({"message": e.errors()}), 400
    except Exception as e:
        jsonify({"message": "Erro durante a requisição."}), 500
    """
    # simulando um login
    if user_data.username == 'admin' and user_data.password == '123':
        return jsonify({"message": "Login bem-sucedido!"})
    else:
        return jsonify({"message": "Credenciais invalidas!"})
    """
    return jsonify({"message":f"Realizar o login do usuário {user_data.model_dump_json()}"})

# RF: O sistema deve permitir listagem de todos os produtos
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = []
    for product in products_cursor:
        # casting do id para string, que originalmete é um ObjectId, que não é json serializable
        product['_id'] = str(product['_id']) 
        products_list.append(product)

    return jsonify(products_list)

# RF: O sistema deve permitir a criacao de um novo produto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"message":"Esta é a rota de criação de produto"})

# RF: O sistema deve permitir a visualizacao dos detalhes de um unico produto
@main_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({"error":f"Erro ao transformar {product_id} em ObjectId: {e}"})
    product = db.products.find_one({'_id':oid})

    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product)
    else:
        return jsonify({"error": f"Produto com o id: {product_id} - Não encontrado"})

# RF: O sistema deve permitir a atualizacao de um unico produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return jsonify({"message":f"Esta é a rota de atualizacao do produto com o id {product_id}"})

# RF: O sistema deve permitir a delecao de um unico produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return jsonify({"message":f"Esta é a rota de deleção do produto com o id {product_id}"})

# RF: O sistema deve permitir a importacao de vendas através de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales():
    return jsonify({"message":"Esta é a rota de upload do arquivo de vendas"})

@main_bp.route('/')
def index():
    return jsonify({"message": "Bem-vindo à API da StyleSync!"})


