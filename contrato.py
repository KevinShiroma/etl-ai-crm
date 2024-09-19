from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Zapflow com Gemini"
    produto2 = "Zapflow com ChatGPT"
    produto3 = "Zapflow com Lhama"


class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    # @validator('produto')
    # def categoria_deve_estar_no_enum(cls,v):
    #     return v