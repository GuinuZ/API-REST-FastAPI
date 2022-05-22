from sqlalchemy import Column, Integer , String 
from infra.sqlalchemy.config.database import Base

class User(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
