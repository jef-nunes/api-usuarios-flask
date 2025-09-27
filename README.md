### Sobre
Protótipo de autenticação de usuário via token JWT, em uma API desenvolvida com o framework Flask. Para a lógica do JWT foi utilizada a biblioteca PyJWT, enquanto para a lógica de acesso ao banco de dados foi utilizada a biblioteca SQL Alchemy.

### Banco de dados
Para o projeto foi escolhido o banco de dados SQLite.

### Respostas da API
As respostas da API foram padronizadas conforme o exemplo abaixo:

```json
{
  "status":"success",
  "data":[],
  "messages":[],
  "timestamp":"26-09-2025 22:46"
}
```

### Endpoints

1. Registrar usuário:
- Método: POST
- Path: /user-register
- Body:
```json
{
  "username":"seu-usuario",
  "password":"sua-senha"
}
```

2. Login:
- Método: POST
- Path: /login
- Body:
```json
{
  "username":"seu-usuario",
  "password":"sua-senha"
}
```
