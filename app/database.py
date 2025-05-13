from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criando a engine de conexão
engine = create_engine(DATABASE_URL)

# Criando a sessão
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Criando as tabelas no banco de dados
Base = declarative_base()

# Função para criar uma nova sessão e garantir o fechamento adequado
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Conexão bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar:", e)
