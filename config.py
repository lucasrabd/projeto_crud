import oracledb

# Inicialize o cliente Oracle se necessário
oracledb.init_oracle_client()

def get_db_connection():
    dsn = oracledb.makedsn("oracle.fiap.com.br", "1521", sid="ord")
    connection = oracledb.connect(user="rm550519", password="020403", dsn=dsn)
    return connection
