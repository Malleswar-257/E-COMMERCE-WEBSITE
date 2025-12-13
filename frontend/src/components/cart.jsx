import React from 'react';
import { useCart } from '../context/CartContext.jsx';
import { useNavigate } from 'react-router-dom';
import './Cart.css';

const Cart = () => {
  const { cart, dispatch } = useCart();
  const navigate = useNavigate();

  const totalPrice = cart.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const totalItems = cart.items.reduce((sum, item) => sum + item.quantity, 0);

  const handlePayment = () => {
    // Navigate to payment page
    navigate('/payment');
  };

  const handleCheckout = () => {
    // Navigate to payment page for checkout
    navigate('/payment');
  };

  return (
    <div className="cart-container">
      <h3 className="cart-title">
        Your Cart ({totalItems} {totalItems === 1 ? 'item' : 'items'})
      </h3>

      {cart.items.length === 0 ? (
        <p className="empty-cart">No items in cart</p>
      ) : (
        <>
          <ul className="cart-list">
            {cart.items.map((item) => (
              <li className="cart-item" key={item.id}>
                <img className="item-image" src={item.image} alt={item.name} />
                <div className="item-details">
                  <span className="item-name">{item.name}</span>
                  <span className="item-qty">Quantity: {item.quantity}</span>
                  <span className="item-price">
                    ₹{(item.price * item.quantity).toLocaleString()}
                  </span>
                </div>
                <div className="item-actions">
                  <button
                    className="payment-btn"
                    onClick={handlePayment}
                  >
                    Pay Now
                  </button>
                  <button
                    className="remove-btn"
                    onClick={() => dispatch({ type: 'REMOVE_FROM_CART', payload: item.id })}
                  >
                    Remove
                  </button>
                </div>
              </li>
            ))}
          </ul>

          <div className="cart-footer">
            <strong className="total-price">Total: ₹{totalPrice.toLocaleString()}</strong>
            <div className="cart-actions">
              <button
                className="checkout-btn"
                onClick={handleCheckout}
              >
                Checkout
              </button>
              <button
                className="clear-btn"
                onClick={() => dispatch({ type: 'CLEAR_CART' })}
              >
                Clear Cart
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default Cart;
