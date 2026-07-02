# 📋 CRUD Clientes e Pedidos — API Python

API Flask com CRUD de clientes e pedidos, persistindo em Azure SQL Database (via `pyodbc`), com interface web simples em HTML/JS puro. Deploy automático via GitHub Actions para Azure Web App.

---

## 📦 Stack

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Azure SQL](https://img.shields.io/badge/Azure%20SQL-Database-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=flat&logo=githubactions&logoColor=white)

---

## 📁 Estrutura do Projeto

```
projeto_crud-main/
├── app.py                                        # Rotas Flask (CRUD de clientes e pedidos)
├── config.py                                       # Conexão com Azure SQL via pyodbc
├── templates/
│   └── index.html                                    # Interface web (formulários + listagem)
├── requirements.txt                                    # Dependências Python
└── .github/workflows/
    ├── main_api-python-2024-3.yml                        # CI/CD → Azure Web App "API-PYTHON-2024-3"
    └── main_api-python-sprint3-rm550519.yml                # CI/CD → Azure Web App "api-python-sprint3-rm550519"
```

> Existem dois workflows de deploy automático (gerados pelo Deployment Center do Azure), cada um publicando em um App Service diferente. Ambos rodam a cada push na branch `main`.

---

## 🔌 Rotas

### Clientes

| Método | Rota | Descrição |
|---|---|---|
| GET | `/clientes` | Lista todos os clientes (`ClienteXYZ`) |
| POST | `/clientes` | Cria um cliente |
| PUT | `/clientes/<id>` | Atualiza um cliente |
| DELETE | `/clientes/<id>` | Remove um cliente |

Corpo esperado (POST/PUT):
```json
{ "ClienteID": 1, "Nome": "string", "Email": "string" }
```

### Pedidos

| Método | Rota | Descrição |
|---|---|---|
| GET | `/pedidos` | Lista todos os pedidos (`PedidosXYZ`) |
| POST | `/pedidos` | Cria um pedido |
| PUT | `/pedidos/<id>` | Atualiza um pedido |
| DELETE | `/pedidos/<id>` | Remove um pedido |

Corpo esperado (POST/PUT):
```json
{ "PedidoID": 1, "ClienteID": 1, "Descricao": "string", "DataPedido": "2026-07-02" }
```

As tabelas `ClienteXYZ` e `PedidosXYZ` precisam existir previamente no banco — o projeto não inclui script de criação (DDL).

---

## 🚀 Como rodar

### Pré-requisitos
- Python 3.12+
- [ODBC Driver 18 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server) instalado na máquina
- Acesso a uma instância Azure SQL Database com as tabelas `ClienteXYZ` e `PedidosXYZ`

### Passos

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure as credenciais do banco via variáveis de ambiente (nunca direto no `config.py`):

```bash
# Linux/Mac
export DB_SERVER="seu-servidor.database.windows.net"
export DB_NAME="sua-database"
export DB_USER="seu-usuario"
export DB_PASSWORD="sua-senha"

# Windows (PowerShell)
$env:DB_SERVER="seu-servidor.database.windows.net"
$env:DB_NAME="sua-database"
$env:DB_USER="seu-usuario"
$env:DB_PASSWORD="sua-senha"
```

3. Execute:

```bash
python app.py
```

4. Acesse `http://127.0.0.1:5000`.

---

## ☁️ Deploy

O deploy é automático via GitHub Actions a cada push em `main`, publicando direto em Azure Web App (`azure/webapps-deploy`). As credenciais do Azure ficam em GitHub Secrets (`AZUREAPPSERVICE_CLIENTID_*`, `TENANTID_*`, `SUBSCRIPTIONID_*`) — configuradas automaticamente pelo Deployment Center do Azure, não precisam ser adicionadas manualmente.

---

## 📄 Licença

Não especificada.
