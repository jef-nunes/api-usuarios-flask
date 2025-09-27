from flask import Flask
from models.user import Base
from routes.user_register import user_register_bp
from routes.login import login_bp
from database.connection import sa_engine
from dotenv import load_dotenv
from services.auth import _get_secret_key

# Carregar o .env
load_dotenv()
print(_get_secret_key())

# Inicializar aplicação Flask
app = Flask(__name__)

# Registrar blueprints no app Flask
app.register_blueprint(user_register_bp)
app.register_blueprint(login_bp)

# Criar tabelas no banco
Base.metadata.create_all(bind=sa_engine)

@app.get("/")
def api_rodando():
    return "A API Flask está rodando..."
