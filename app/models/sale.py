from pydantic import BaseModel,  ConfigDict
from datetime import datetime

class Sale(BaseModel):
    sale_date: datetime
    product_id: str
    quantity: int
    total_value: float

    model_config = ConfigDict(
        populate_by_name= True, # permite a instanciação de Product() tanto com atributo "id" Como "_id"
        arbitrary_types_allowed=True # permite usar e validar tipos personalizados, como "ObjectId"
    )