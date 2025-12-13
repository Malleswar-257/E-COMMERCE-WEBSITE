// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CustomNavbar from './components/navbar';
import Home from './pages/home';
import Profile from './components/profile';
import Cart from './components/cart';
import PaymentPage from './pages/PaymentPage';
import { CartProvider } from './context/CartContext';
import ProductList from './data/ProductList';

function App() {
  return (
    <CartProvider>
      <Router>
        <div className="app-layout">
          <CustomNavbar />
          <Routes>
            <Route
              path="/"
              element={
                <>
                  <Home />
                  <ProductList />
                </>
              }
            />
            <Route path="/profile" element={<Profile />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/payment" element={<PaymentPage />} />
          </Routes>
        </div>
      </Router>
    </CartProvider>
  );
}

export default App;
