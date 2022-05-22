from sqlalchemy.orm import Session
from infra.schemas import schemas
from infra.sqlalchemy.models import models

class RepositorioUsuario():

    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, usuario: schemas.Usuario ):
        db_usuario = models.User(nome=usuario.nome,senha=usuario.senha)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def obter(self):
        usuarios = self.db.query(models.User).all()
        return usuarios
