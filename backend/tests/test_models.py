from app.models import User, Product, Cart, Order

def test_user_model():
    user = User(email='user@example.com', password='password')
    assert user.email == 'user@example.com'
    assert user.password == 'password'

def test_product_model():
    product = Product(name='Product 1', price=10.99)
    assert product.name == 'Product 1'
    assert product.price == 10.99

def test_cart_model():
    cart = Cart(user_id=1, product_id=1, quantity=2)
    assert cart.user_id == 1
    assert cart.product_id == 1
    assert cart.quantity == 2

def test_order_model():
    order = Order(customer_id=1, order_date='2022-01-01')
    assert order.customer_id == 1
    assert order.order_date == '2022-01-01'