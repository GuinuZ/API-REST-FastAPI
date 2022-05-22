from fastapi import FastAPI , Depends
from infra.sqlalchemy.config.database import get_db, criar_db
from infra.sqlalchemy.repositorios.user import RepositorioUsuario
from infra.schemas import schemas
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

criar_db()

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/usuarios')
def listarUsuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).obter()
    return usuarios

@app.post('/usuarios')
def criarUsuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
