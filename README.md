# 🚀 Projeto DevOps -- Flask API com JWT, Docker, Testes e Deploy no Render

Este projeto foi desenvolvido como parte do desafio final da disciplina
de DevOps, aplicando os principais conceitos da cultura DevOps:
**Build**, **Test** e **Deploy**.

A aplicação consiste em uma API Flask simples com autenticação JWT,
documentada com Swagger UI, testada com `unittest`, empacotada em
Docker, validada por CI no GitHub Actions e publicada automaticamente no
Render (CD).

------------------------------------------------------------------------

# 🌐 Acesso à API em Produção

  Recurso          URL
  ---------------- ----------------------------------------------
  **API Online**   https://lab-devops-api.onrender.com
  **Swagger UI**   https://lab-devops-api.onrender.com/swagger/

------------------------------------------------------------------------

# 📁 Estrutura do Projeto

    lab-devops-api/
    ├── app.py
    ├── static/
    │   └── swagger.json
    ├── test_app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    └── .github/
        └── workflows/
            └── ci.yml

------------------------------------------------------------------------

# 🔧 1. Tecnologias Utilizadas

-   **Flask 2.3.2**
-   **JWT (Flask-JWT-Extended)**
-   **Swagger UI**
-   **Python 3.9**
-   **Docker / Docker Compose**
-   **GitHub Actions (CI)**
-   **Render (CD -- Deploy automático)**
-   **Unittest**

------------------------------------------------------------------------

# 🧪 2. Testes Automatizados (`unittest`)

Foram implementados 6 testes cobrindo:

✔ `/` --- status e mensagem\
✔ `/items` --- integridade da lista\
✔ `/login` --- geração de token JWT\
✔ `/protected` --- rota protegida com token válido\
✔ `/protected` --- acesso negado sem token\
✔ Rota inexistente --- retorno `404`

### Rodar testes localmente:

``` bash
python -m unittest -v
```

### Rodar testes via Docker:

``` bash
docker run --rm devops-api python -m unittest -v
```

------------------------------------------------------------------------

# 📦 3. Build e Execução com Docker

### Criar imagem:

``` bash
docker build -t devops-api .
```

### Executar container:

``` bash
docker run -p 1313:1313 devops-api
```

### Usando Docker Compose:

``` bash
docker compose up --build
```

------------------------------------------------------------------------

# 🔄 4. Pipeline CI -- GitHub Actions

Arquivo: `.github/workflows/ci.yml`

O CI executa:

1.  Instala dependências
2.  Roda os testes (`unittest`)
3.  Build da imagem Docker
4.  Executa os testes *dentro do container*

O deploy só é acionado após o CI passar com sucesso.

------------------------------------------------------------------------

# 🚀 5. Deploy Contínuo (CD) -- Render

A aplicação é publicada automaticamente no Render quando há push na
branch `main`.

O Render utiliza:

-   Dockerfile como blueprint

-   Porta exposta `1313`

-   Variável de ambiente:

        JWT_SECRET_KEY=super-secret-key-devops

API acessível em produção:

👉 https://lab-devops-api.onrender.com\
👉 https://lab-devops-api.onrender.com/swagger/

------------------------------------------------------------------------

# 🔑 6. Como utilizar autenticação JWT no Swagger

### 1. Vá até a rota `/login`

Clique em **Execute**\
Ela retorna:

``` json
{
  "access_token": "<seu_token>"
}
```

### 2. Clique no botão **Authorize**

Cole assim:

    Bearer <token>

### 3. Agora abra `/protected`

Clique em **Execute**

Retorno esperado:

``` json
{
  "message": "Protected route"
}
```

Autenticação funcionando! 🔥

------------------------------------------------------------------------

# 🛠 7. Arquivos Principais

### `Dockerfile`

Empacota a aplicação para rodar em produção.

### `docker-compose.yml`

Ambiente de desenvolvimento.

### `test_app.py`

Testes automatizados.

### `swagger.json`

Documentação da API (sem host fixo --- compatível com ambiente local e
nuvem).

------------------------------------------------------------------------

# 📈 8. Fluxo CI/CD -- DevOps

    Git Push →
        GitHub Actions (CI):
            - Install
            - Test
            - Docker Build
            - Test no Docker
        →
    Render (CD):
        - Build da imagem
        - Deploy automático
        - API online

------------------------------------------------------------------------

# 👤 Autor

**Geovane Soares da Silva**\
Github: https://github.com/Gesoaress\
Projeto: https://github.com/Gesoaress/lab-devops-api

------------------------------------------------------------------------

# 🎯 Conclusão

Este projeto demonstra um pipeline DevOps completo, aplicando práticas
modernas de integração contínua, entrega contínua, testes automatizados,
containerização com Docker e deploy em nuvem com Render.\
O resultado é uma API estável, testada, versionada, automatizada e
disponível publicamente.
