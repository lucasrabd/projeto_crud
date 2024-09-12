from flask import Flask, request, jsonify, render_template
from config import get_db_connection

app = Flask(__name__)

# Rota para servir o arquivo HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter todos os clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ClienteXYZ")
    clientes = cursor.fetchall()
    conn.close()
    return jsonify([{"ClienteID": row[0], "Nome": row[1], "Email": row[2]} for row in clientes])

# Rota para criar um novo cliente
@app.route('/clientes', methods=['POST'])
def create_cliente():
    new_cliente = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ClienteXYZ (ClienteID, Nome, Email) VALUES (?, ?, ?)",
                   (new_cliente['ClienteID'], new_cliente['Nome'], new_cliente['Email']))
    conn.commit()
    conn.close()
    return '', 201

# Rota para atualizar um cliente existente
@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    update_cliente = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE ClienteXYZ SET Nome = ?, Email = ? WHERE ClienteID = ?",
                   (update_cliente['Nome'], update_cliente['Email'], id))
    conn.commit()
    conn.close()
    return '', 204

# Rota para deletar um cliente
@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ClienteXYZ WHERE ClienteID = ?", (id,))
    conn.commit()
    conn.close()
    return '', 204

# Rota para obter todos os pedidos
@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PedidosXYZ")
    pedidos = cursor.fetchall()
    conn.close()
    return jsonify([{"PedidoID": row[0], "ClienteID": row[1], "Descricao": row[2], "DataPedido": row[3]} for row in pedidos])

# Rota para criar um novo pedido
@app.route('/pedidos', methods=['POST'])
def create_pedido():
    new_pedido = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PedidosXYZ (PedidoID, ClienteID, Descricao, DataPedido) VALUES (?, ?, ?, ?)",
                   (new_pedido['PedidoID'], new_pedido['ClienteID'], new_pedido['Descricao'], new_pedido['DataPedido']))
    conn.commit()
    conn.close()
    return '', 201

# Rota para atualizar um pedido existente
@app.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    update_pedido = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE PedidosXYZ SET ClienteID = ?, Descricao = ?, DataPedido = ? WHERE PedidoID = ?",
                   (update_pedido['ClienteID'], update_pedido['Descricao'], update_pedido['DataPedido'], id))
    conn.commit()
    conn.close()
    return '', 204

# Rota para deletar um pedido
@app.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PedidosXYZ WHERE PedidoID = ?", (id,))
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
