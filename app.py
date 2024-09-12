from flask import Flask, request, jsonify, render_template
from config import get_db_connection

app = Flask(__name__)

# Rota para servir o arquivo HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ClienteXYZ")
    clientes = cursor.fetchall()
    conn.close()
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def create_cliente():
    new_cliente = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ClienteXYZ (ClienteID, Nome, Email) VALUES (:1, :2, :3)",
                   (new_cliente['ClienteID'], new_cliente['Nome'], new_cliente['Email']))
    conn.commit()
    conn.close()
    return '', 201

@app.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    update_cliente = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE ClienteXYZ SET Nome = :1, Email = :2 WHERE ClienteID = :3",
                   (update_cliente['Nome'], update_cliente['Email'], id))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ClienteXYZ WHERE ClienteID = :1", (id,))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PedidosXYZ")
    pedidos = cursor.fetchall()
    conn.close()
    return jsonify(pedidos)

@app.route('/pedidos', methods=['POST'])
def create_pedido():
    new_pedido = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PedidosXYZ (PedidoID, ClienteID, Descricao, DataPedido) VALUES (:1, :2, :3, :4)",
                   (new_pedido['PedidoID'], new_pedido['ClienteID'], new_pedido['Descricao'], new_pedido['DataPedido']))
    conn.commit()
    conn.close()
    return '', 201

@app.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    update_pedido = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE PedidosXYZ SET ClienteID = :1, Descricao = :2, DataPedido = :3 WHERE PedidoID = :4",
                   (update_pedido['ClienteID'], update_pedido['Descricao'], update_pedido['DataPedido'], id))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM PedidosXYZ WHERE PedidoID = :1", (id,))
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
