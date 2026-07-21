from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    id: Optional[ObjectId] = Field(None, alias='_id') #estamos dizendo: valor padrão = None; este atributo corresponde ao campo _id (dos objetos do mongo)
    name: str
    brand: str
    category: str
    description: Optional[str] = None
    price: float
    stock: int

    model_config = ConfigDict(
        populate_by_name= True, # permite a instanciação de Product() tanto com atributo "id" Como "_id"
        arbitrary_types_allowed=True # permite usar e validar tipos personalizados, como "ObjectId"
    )

class ProductDBModel(Product):

    # leitura dos dados do banco de dados e converção do resultado em JSON
        # resolve o problema de converter campo ObjectId (not serializable by json) para json

    # model_dump() transforma um modelo Pydantic em um dicionário
        # model_dump() é função de BaseModel
        # aqui estamos modificando a função model_dump() com casting de id (ObjectId) para string
    def model_dump(self, *, mode='python', include=None, exclude=None, context=None, by_alias=None, exclude_unset=False, exclude_defaults=False, exclude_none=False, round_trip=False):
        # super().model_dump() chama a model de Product (herdade de BaseModel)
        data = super().model_dump(mode=mode, include=include, exclude=exclude, context=context, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, round_trip=round_trip)
        if self.id:
            data["_id"] = str(data["_id"]) # casting de id para string
        return data

class UpdateProduct(BaseModel):

    # atualização de dados 

    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    stock: Optional[int] = None

class QueryProduct(BaseModel):

    # Validação de parâmetros da query
    # Criação da query para o mongodb (filtros, paginação e ordenação)

    # pages
    page: Optional[int] = 1
    limit: Optional[int] = 20
    
    # filters
    category: Optional[str] = None
    brand: Optional[str] = None
    price_min: Optional[int] = None
    price_max: Optional[int] = None
    stock_min: Optional[int] = None

    # search
    search: Optional[str] = None

    # sorting
    sort: Optional[str] = None

    def build_mongo_query(self):
        query = {}

        if self.category:
            query["category"] = {
                        "$regex": self.category,
                        "$options": "i"
                    }
        if self.brand:
            query["brand"] = {
                        "$regex": self.brand,
                        "$options": "i"
                    }

        if self.price_min or self.price_max:
            query["price"] = {}

            if self.price_min is not None:
                query["price"]["$gte"] = self.price_min

            if self.price_max is not None:
                query["price"]["$lte"] = self.price_max

        if self.stock_min:
            query["stock"] = {"$gte": self.stock_min}
        
        if self.search:
            query["$or"] = [
                {
                    "name": {
                        "$regex": self.search,
                        "$options": "i"
                    }
                },
                {
                    "description": {
                        "$regex": self.search,
                        "$options": "i"
                    }
                }
            ]
        return query

    def apply_sort(self, products_cursor):
        sorted_cursor = products_cursor
        if self.sort == "price":
            sorted_cursor = products_cursor.sort("price", 1)
        elif self.sort == "-price":
            sorted_cursor = products_cursor.sort("price", -1)
        return sorted_cursor
    
    def apply_pagination(self, products_cursor):
        paginated_cursor = products_cursor.skip((self.page - 1) * self.limit).limit(self.limit)
        return paginated_cursor