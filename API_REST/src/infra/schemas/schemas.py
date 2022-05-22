from pydantic import BaseModel
from typing import Optional


class Usuario(BaseModel):
    id: Optional[int]
    nome: str
    senha: str

    class Config:
        orm_mode = True

