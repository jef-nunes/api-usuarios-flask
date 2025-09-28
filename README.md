### Sobre
Autenticação de usuário em uma API desenvolvida com Flask, utilizando token JWT para essa finalidade. Para a lógica do JWT foi utilizada a biblioteca PyJWT, enquanto para a lógica de acesso ao banco de dados foi utilizada a biblioteca SQL Alchemy.
<br>
<br>

### Banco de dados
Para o projeto foi escolhido o banco de dados SQLite.
<br>
<br>

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
<br>
<br>

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
