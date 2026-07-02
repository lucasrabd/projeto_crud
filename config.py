import os
import pyodbc


def get_db_connection():
    # Configuração da cadeia de conexão — lida de variáveis de ambiente,
    # nunca deixe usuário/senha reais direto no código versionado.
    server = os.environ.get('DB_SERVER', 'seu-servidor.database.windows.net')
    database = os.environ.get('DB_NAME', 'sua-database')
    username = os.environ.get('DB_USER', 'seu-usuario')
    password = os.environ.get('DB_PASSWORD', 'sua-senha')
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
