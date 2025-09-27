from flask import Blueprint, request
from models.user import User
from database.connection import make_sa_session
from services.hashing import hash_password
from services.validation import validate_password, validate_username
from .util.response_builder import build_response
from http import HTTPStatus

user_register_bp = Blueprint("user_register", __name__)

@user_register_bp.route("/user-register", methods=["POST"])
def user_register_endpoint():
    
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
        password_hash, salt = hash_password(password)
        new_user = User(username=username, password_hash=password_hash,salt=salt)
        sa_session = make_sa_session()
        sa_session.add(new_user)
        sa_session.commit()
        return build_response(HTTPStatus.CREATED, True, data={"username":username},messages=["Usuário criado com sucesso."])
    
    except Exception as ex:
        print(ex)
        return build_response(HTTPStatus.INTERNAL_SERVER_ERROR, False,messages=["Erro ao criar um novo usuário, tente novamente."])
    
    finally:
        sa_session.close()