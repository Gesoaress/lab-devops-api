# 🚀 Flask DevOps API – Docker • Unittest • GitHub Actions • Render

Este projeto implementa uma API Flask completa, com autenticação JWT, documentação Swagger, testes automatizados, containerização via Docker e pipeline CI/CD com três jobs separados: **build**, **test** e **deploy**.

O deploy final é realizado automaticamente pela plataforma **Render**, sempre que há um push na branch `main`.

---

# 📌 Acesso à Aplicação

- 🌐 **API em Produção:**  
  https://lab-devops-api.onrender.com

- 📘 **Swagger UI (Documentação):**  
  https://lab-devops-api.onrender.com/swagger/

---

# 📂 Estrutura do Projeto

```
lab-devops-api/
 ├── app.py
 ├── test_app.py
 ├── requirements.txt
 ├── Dockerfile
 ├── docker-compose.yml
 ├── static/
 │    └── swagger.json
 └── .github/
      └── workflows/
            └── ci.yml
```

---

# ⚙️ Tecnologias Utilizadas

- **Python 3.9**
- **Flask**
- **JWT (Flask-JJWT-Extended)**
- **Swagger UI**
- **Docker**
- **Unittest**
- **GitHub Actions – CI/CD**
- **Render – Deploy automático**

---

# 🧪 Testes Automatizados (unittest + Docker)

Todos os testes são executados **dentro do Docker**, garantindo que o ambiente é idêntico ao de produção.

Os testes cobrem:

- `/` → status da API  
- `/items` → retorno da lista  
- `/login` → geração de JWT  
- `/protected` → token válido e inválido  
- Rota inexistente → retorna 404  

Arquivo: `test_app.py`

---

# 📦 Docker

### 🔧 Build da imagem

```bash
docker build -t devops-api .
```

### ▶️ Executar container localmente

```bash
docker run -p 1313:1313 devops-api
```

---

# 🧬 Pipeline CI/CD (GitHub Actions)

O pipeline é composto por **3 jobs independentes**, seguindo o ciclo DevOps:

```
BUILD → TEST → DEPLOY
```

---

# 🛠️ Arquivo completo do workflow (ci.yml)

```yaml
name: CI - Flask DevOps API

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  # ========================
  # 1) JOB DE BUILD
  # ========================
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout do código
        uses: actions/checkout@v4

      - name: Build da imagem Docker
        run: |
          docker build -t devops-api:${{ github.sha }} .

  # ========================
  # 2) JOB DE TEST
  # ========================
  test:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout do código
        uses: actions/checkout@v4

      - name: Build da imagem Docker para testes
        run: |
          docker build -t devops-api-test:${{ github.sha }} .

      - name: Rodar testes dentro do Docker
        run: |
          docker run --rm devops-api-test:${{ github.sha }} python -m unittest -v

  # ========================
  # 3) JOB DE DEPLOY
  # ========================
  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'

    steps:
      - name: Fase de Deploy
        run: |
          echo "Deploy feito automaticamente pelo Render."
```

---

# 📘 Swagger

A documentação está no arquivo:

```
static/swagger.json
```

E acessível em:

https://lab-devops-api.onrender.com/swagger/

---

# 🔐 Autenticação JWT

A rota `/login` retorna o token:

```json
{
  "access_token": "<TOKEN>"
}
```

Para acessar `/protected`, é obrigatório enviar:

```
Authorization: Bearer <TOKEN>"
```

---

# 🧾 Conclusão

Este projeto demonstra um ambiente DevOps completo, estruturado com:

- Build → Test → Deploy  
- Testes isolados no Docker  
- Deploy automático no Render  
- Documentação Swagger  
- Autenticação JWT  
- Pipeline CI/CD organizado e profissional  
