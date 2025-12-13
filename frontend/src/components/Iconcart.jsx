import React from 'react';
import { useCart } from '../context/CartContext';
import './CartIcon.css'; 

const CartIcon = () => {
  const { cart } = useCart();
  const totalItems = cart.items.reduce((sum, item) => sum + item.quantity, 0);

  return (
    <div className="cart-icon-container">
      <div className="icon-wrapper">
        <span className="cart-image">🛒</span>
        {totalItems > 0 && (
          <span className="cart-count">{totalItems}</span>
        )}
      </div>
      <span className="cart-label">Cart</span>
    </div>
  );
};

export default CartIcon;
