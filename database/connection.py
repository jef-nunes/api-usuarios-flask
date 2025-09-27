from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.orm import sessionmaker as sa_sessionmaker
#import sqlite3

# Criar o banco de dados se não existir
#_conn = sqlite3.connect("./database/sqlite.db")
#_conn.close()

# URL do banco de dados
DATABASE_URL = "sqlite:///database/sqlite.db"

# Configurar SQLAlchemy
sa_engine = sa_create_engine(DATABASE_URL, echo=True)
make_sa_session = sa_sessionmaker(autoflush=False, bind=sa_engine)