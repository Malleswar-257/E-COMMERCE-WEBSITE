from sqlalchemy.orm import Session from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth_utils.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_products(db: Session):
    return db.query(models.Product).all()
def get_cart_items_by_user_id(db: Session, user_id: int):
    cart = db.query(models.Cart).filter(models.Cart.user_id == user_id).first()
    if not cart:
        return []
    return db.query(models.CartItem).filter(models.CartItem.cart_id == cart.id).all()
def create_order(db: Session, user, items):
    order = models.Order(user_id=user.id, status="pending")
    db.add(order)
    for item in items:
        order_item = models.OrderItem(order=order, product_id=item.product_id, quantity=item.quantity)
        db.add(order_item)
    db.commit()
    db.refresh(order)
    return order