import pyodbc

def get_db_connection():
    # Configuração da cadeia de conexão
    server = 'server-sql-sprint3-rm550519.database.windows.net'
    database = 'API-NET-SPRINT3-SQLDB'
    username = 'adm-sqldb-dimdim'
    password = 'Fiap@2tdsdb'  # Senha fornecida
    driver = '{ODBC Driver 18 for SQL Server}'  # Certifique-se de que o driver correto está instalado

    try:
        # Estabelecendo a conexão
        conn = pyodbc.connect(
            f'Driver={driver};'
            f'Server={server};'
            f'Port=1433;'
            f'Database={database};'
            f'Uid={username};'
            f'Pwd={password};'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            'Connection Timeout=30;'
        )
        return conn  # Retorna a conexão estabelecida

    except pyodbc.Error as e:
        print(f"Erro ao conectar ao SQL Server: {e}")
        return None
