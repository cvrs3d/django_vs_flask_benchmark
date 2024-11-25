from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
import os

# Мы используем существующие таблицы и поэтому надо поебаться
app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
  # Use your database URI here
db = SQLAlchemy(app)


# Определение связывающей таблицы order_products
order_products = db.Table('testing_order_products',  # предполагаем, что имя сводной таблицы 'testing_order_products'
                          db.Column('order_id', db.Integer, db.ForeignKey('testing_order.id'), primary_key=True),
                          db.Column('product_id', db.Integer, db.ForeignKey('testing_product.id'), primary_key=True)
                          )


class Order(db.Model):
    __tablename__ = 'testing_order'  # указываем существующее имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('testing_customer.id'))
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    products = db.relationship('Product', secondary=order_products, lazy='subquery',
                               backref=db.backref('orders', lazy=True))


class Product(db.Model):
    __tablename__ = 'testing_product'  # указываем существующее имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2), nullable=False)
    # другие поля...


class Customer(db.Model):
    __tablename__ = 'testing_customer'  # указываем существующее имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/api/orders/<int:order_id>/', methods=['GET'])
def get_order(order_id):
    # Получаем заказ по ID
    order = Order.query.get(order_id)

    # Если заказ не найден, возвращаем 404
    if order is None:
        return jsonify({"error": "Order not found"}), 404

    # Формируем ответ в формате JSON, аналогичный Django
    data = {
        'order': {
            'id': order.id,
            'created_at': order.created_at,
            'customer': {
                'id': order.customer.id,
                'name': order.customer.name,
                'email': order.customer.email,
            },
            'products': [
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                } for product in order.products
            ]
        },
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

