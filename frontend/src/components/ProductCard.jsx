import React from 'react';
import { useCart } from '../context/CartContext';
import './ProductCard.css';

const ProductCard = ({ product }) => {
  const { dispatch } = useCart();

  return (
    <div className="product-card">
      <img src={product.image} alt={product.name} />
      <h4>{product.name}</h4>
      <p>₹{product.price.toLocaleString()}</p>
      <div className="buttons">
        <button onClick={() => dispatch({ type: 'ADD_TO_CART', payload: product })}>
          Add to Cart
        </button>
        <button className="buy-btn">Buy Now</button>
      </div>
    </div>
  );
};

export default ProductCard;
