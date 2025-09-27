from flask import Blueprint, request
from models.user import User
from services.validation import validate_password, validate_username
from .util.response_builder import build_response
from http import HTTPStatus
from services.auth import verify_password, generate_jwt
from database.connection import make_sa_session

login_bp = Blueprint("login", __name__)

# Endpoint onde o usuário envia credenciais para login
# em caso de sucesso é retornado um token JWT
@login_bp.route("/login", methods=["POST"])
def user_login_endpoint():

    data = request.json

    username = data["username"]
    password = data["password"]

    response_error_messages = []

    request_is_valid = True
    is_valid_username, msg_username_validation = validate_username(username)
    is_valid_password, msg_password_validation = validate_password(password)

    if not is_valid_username:
        response_error_messages.append(msg_username_validation)
        request_is_valid = False
    
    if not is_valid_password:
        response_error_messages.append(msg_password_validation)
        request_is_valid = False

    if not request_is_valid:
        return build_response(HTTPStatus.BAD_REQUEST,False,messages=response_error_messages)
    
    try:

        sa_session = make_sa_session()

        user = sa_session.query(User).filter_by(username=username).first()

        if not user:
            return build_response(HTTPStatus.NOT_FOUND, False, messages=["Usuário não registrado."])
        
        if not verify_password(password,user.password_hash,user.salt):
            return build_response(HTTPStatus.UNAUTHORIZED, False, messages=["Credenciais inválidas."])
        
        token = generate_jwt(user.id)

        return build_response(HTTPStatus.OK, True, data={"token":token})
    
    finally:
        sa_session.close()
        
