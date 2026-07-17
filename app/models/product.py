from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    id: Optional[ObjectId] = Field(None, alias='_id') #estamos dizendo: valor padrão = None; este atributo corresponde ao campo _id (dos objetos do mongo)
    name: str
    price: float
    description: Optional[str] = None
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