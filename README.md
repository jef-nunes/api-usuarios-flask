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

### Endpoints de registrar usuário e de login
Para registrar um usuário é necessário fazer uma requisição POST na rota "/user-register", com o body contendo o nome de usuário no campo "username" e a senha no campo "password"

O endpoint de login utiliza o método POST na rota "/user-login", passando no body da requisição os mesmos campos do endpoint de registro de usuário. Em caso de login bem sucedido o token JWT é retornado no campo "data".
