import re

# Validar nome de usuário
def validate_username(username: str):

    if not username:
        return False, "O campo username não pode estar vazio."
    
    if len(username)<3 or len(username)>30:
        return False, "O campo username deve ter entre 3 e 30 caracteres."
    
    if not re.match(r'^[a-zA-Z0-9_.]+$', username):
        return False, "O campo username pode conter apenas letras, números, underscores e pontos."
    
    return True, "Username válido."



# Validar senha
def validate_password(password: str):

    if not password:
        return False, "O campo password não pode estar vazio."
    
    if len(password)<8 or len(password)>255:
        return False, "O campo password deve ter entre 8 e 255 caracteres"
    
    if not re.match(r'^[A-Za-z0-9@#$!%-_]+$',password):
        return False, "O campo password pode ter apenas letras, números e os seguintes símbolos: @#$!%-_"
    
    return True, "Senha válida."