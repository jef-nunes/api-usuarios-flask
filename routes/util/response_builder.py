from flask import jsonify
from datetime import datetime

# Criar uma response JSON padronizada
def build_response(status_code: int, success: bool, data=None, messages=[]):

    if success:
        status = "success"
    else:
        status = "failure"

    if status_code is None:
        print("O argumento status_code em response_builder.success_response() é obrigatório.")

    payload = {
        "status": status,
        "data": data,
        "messages": messages,
        "timestamp": datetime.now()
    }

    return jsonify(payload), status_code