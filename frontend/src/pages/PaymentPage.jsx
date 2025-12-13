import React, { useState } from 'react';
import { useCart } from '../context/CartContext';
import { useNavigate, useLocation } from 'react-router-dom';
import './PaymentPage.css';

const PaymentPage = () => {
  const { cart, dispatch } = useCart();
  const navigate = useNavigate();
  const location = useLocation();
  
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('upi');
  const [deliveryAddress, setDeliveryAddress] = useState({
    name: '',
    phone: '',
    address: '',
    city: '',
    state: '',
    pincode: ''
  });

  // Payment details state
  const [paymentDetails, setPaymentDetails] = useState({
    upi: {
      upiId: '',
      upiApp: 'gpay'
    },
    card: {
      cardNumber: '',
      cardHolder: '',
      expiryMonth: '',
      expiryYear: '',
      cvv: ''
    },
    netbanking: {
      bankName: '',
      accountNumber: ''
    },
    cod: {
      // No additional details needed for COD
    }
  });

  const totalPrice = cart.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const totalItems = cart.items.reduce((sum, item) => sum + item.quantity, 0);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setDeliveryAddress(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handlePaymentDetailsChange = (e) => {
    const { name, value } = e.target;
    setPaymentDetails(prev => ({
      ...prev,
      [selectedPaymentMethod]: {
        ...prev[selectedPaymentMethod],
        [name]: value
      }
    }));
  };

  const handlePayment = () => {
    if (!deliveryAddress.name || !deliveryAddress.phone || !deliveryAddress.address) {
      alert('Please fill in all required delivery details');
      return;
    }

    // Validate payment details based on selected method
    const currentPaymentDetails = paymentDetails[selectedPaymentMethod];
    let isValid = true;
    let errorMessage = '';

    switch (selectedPaymentMethod) {
      case 'upi':
        if (!currentPaymentDetails.upiId) {
          isValid = false;
          errorMessage = 'Please enter UPI ID';
        }
        break;
      case 'card':
        if (!currentPaymentDetails.cardNumber || !currentPaymentDetails.cardHolder || 
            !currentPaymentDetails.expiryMonth || !currentPaymentDetails.expiryYear || 
            !currentPaymentDetails.cvv) {
          isValid = false;
          errorMessage = 'Please fill in all card details';
        }
        break;
      case 'netbanking':
        if (!currentPaymentDetails.bankName || !currentPaymentDetails.accountNumber) {
          isValid = false;
          errorMessage = 'Please fill in all net banking details';
        }
        break;
      case 'cod':
        // No validation needed for COD
        break;
      default:
        isValid = false;
        errorMessage = 'Please select a payment method';
    }

    if (!isValid) {
      alert(errorMessage);
      return;
    }
    
    // Simulate payment processing
    alert('Payment processing... Order placed successfully!');
    dispatch({ type: 'CLEAR_CART' });
    navigate('/');
  };

  const renderPaymentDetails = () => {
    switch (selectedPaymentMethod) {
      case 'upi':
        return (
          <div className="payment-details-form">
            <h4>UPI Payment Details</h4>
            <div className="form-group">
              <label>UPI ID *</label>
              <input
                type="text"
                name="upiId"
                placeholder="Enter UPI ID (e.g., user@upi)"
                value={paymentDetails.upi.upiId}
                onChange={handlePaymentDetailsChange}
                required
              />
            </div>
            <div className="form-group">
              <label>UPI App</label>
              <select
                name="upiApp"
                value={paymentDetails.upi.upiApp}
                onChange={handlePaymentDetailsChange}
              >
                <option value="gpay">Google Pay</option>
                <option value="phonepe">PhonePe</option>
                <option value="paytm">Paytm</option>
                <option value="amazonpay">Amazon Pay</option>
                <option value="other">Other</option>
              </select>
            </div>
          </div>
        );

      case 'card':
        return (
          <div className="payment-details-form">
            <h4>Card Payment Details</h4>
            <div className="form-group">
              <label>Card Number *</label>
              <input
                type="text"
                name="cardNumber"
                placeholder="1234 5678 9012 3456"
                value={paymentDetails.card.cardNumber}
                onChange={handlePaymentDetailsChange}
                maxLength="19"
                required
              />
            </div>
            <div className="form-group">
              <label>Card Holder Name *</label>
              <input
                type="text"
                name="cardHolder"
                placeholder="Name on card"
                value={paymentDetails.card.cardHolder}
                onChange={handlePaymentDetailsChange}
                required
              />
            </div>
            <div className="form-row">
              <div className="form-group">
                <label>Expiry Month *</label>
                <select
                  name="expiryMonth"
                  value={paymentDetails.card.expiryMonth}
                  onChange={handlePaymentDetailsChange}
                  required
                >
                  <option value="">MM</option>
                  {Array.from({length: 12}, (_, i) => i + 1).map(month => (
                    <option key={month} value={month.toString().padStart(2, '0')}>
                      {month.toString().padStart(2, '0')}
                    </option>
                  ))}
                </select>
              </div>
              <div className="form-group">
                <label>Expiry Year *</label>
                <select
                  name="expiryYear"
                  value={paymentDetails.card.expiryYear}
                  onChange={handlePaymentDetailsChange}
                  required
                >
                  <option value="">YYYY</option>
                  {Array.from({length: 10}, (_, i) => new Date().getFullYear() + i).map(year => (
                    <option key={year} value={year}>{year}</option>
                  ))}
                </select>
              </div>
              <div className="form-group">
                <label>CVV *</label>
                <input
                  type="password"
                  name="cvv"
                  placeholder="123"
                  value={paymentDetails.card.cvv}
                  onChange={handlePaymentDetailsChange}
                  maxLength="4"
                  required
                />
              </div>
            </div>
          </div>
        );

      case 'netbanking':
        return (
          <div className="payment-details-form">
            <h4>Net Banking Details</h4>
            <div className="form-group">
              <label>Select Bank *</label>
              <select
                name="bankName"
                value={paymentDetails.netbanking.bankName}
                onChange={handlePaymentDetailsChange}
                required
              >
                <option value="">Select your bank</option>
                <option value="sbi">State Bank of India</option>
                <option value="hdfc">HDFC Bank</option>
                <option value="icici">ICICI Bank</option>
                <option value="axis">Axis Bank</option>
                <option value="kotak">Kotak Mahindra Bank</option>
                <option value="yes">Yes Bank</option>
                <option value="pnb">Punjab National Bank</option>
                <option value="bob">Bank of Baroda</option>
                <option value="canara">Canara Bank</option>
                <option value="union">Union Bank of India</option>
              </select>
            </div>
            <div className="form-group">
              <label>Account Number *</label>
              <input
                type="text"
                name="accountNumber"
                placeholder="Enter account number"
                value={paymentDetails.netbanking.accountNumber}
                onChange={handlePaymentDetailsChange}
                required
              />
            </div>
          </div>
        );

      case 'cod':
        return (
          <div className="payment-details-form">
            <h4>Cash on Delivery</h4>
            <div className="cod-info">
              <p>💰 Pay when you receive your order</p>
              <p>💳 No additional charges</p>
              <p>📦 Delivery within 3-5 business days</p>
            </div>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="payment-container">
      <div className="payment-header">
        <h2>Payment</h2>
        <div className="breadcrumb">
          <span>Cart</span> → <span>Delivery</span> → <span className="active">Payment</span>
        </div>
      </div>

      <div className="payment-content">
        <div className="payment-left">
          {/* Delivery Address */}
          <div className="section">
            <h3>Delivery Address</h3>
            <div className="address-form">
              <div className="form-row">
                <input
                  type="text"
                  name="name"
                  placeholder="Full Name *"
                  value={deliveryAddress.name}
                  onChange={handleInputChange}
                  required
                />
                <input
                  type="tel"
                  name="phone"
                  placeholder="Phone Number *"
                  value={deliveryAddress.phone}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <textarea
                name="address"
                placeholder="Delivery Address *"
                value={deliveryAddress.address}
                onChange={handleInputChange}
                required
              />
              <div className="form-row">
                <input
                  type="text"
                  name="city"
                  placeholder="City"
                  value={deliveryAddress.city}
                  onChange={handleInputChange}
                />
                <input
                  type="text"
                  name="state"
                  placeholder="State"
                  value={deliveryAddress.state}
                  onChange={handleInputChange}
                />
                <input
                  type="text"
                  name="pincode"
                  placeholder="Pincode"
                  value={deliveryAddress.pincode}
                  onChange={handleInputChange}
                />
              </div>
            </div>
          </div>

          {/* Payment Methods */}
          <div className="section">
            <h3>Payment Options</h3>
            <div className="payment-methods">
              <div className="payment-option">
                <input
                  type="radio"
                  id="upi"
                  name="paymentMethod"
                  value="upi"
                  checked={selectedPaymentMethod === 'upi'}
                  onChange={(e) => setSelectedPaymentMethod(e.target.value)}
                />
                <label htmlFor="upi">
                  <span className="payment-icon">📱</span>
                  UPI
                </label>
              </div>
              
              <div className="payment-option">
                <input
                  type="radio"
                  id="card"
                  name="paymentMethod"
                  value="card"
                  checked={selectedPaymentMethod === 'card'}
                  onChange={(e) => setSelectedPaymentMethod(e.target.value)}
                />
                <label htmlFor="card">
                  <span className="payment-icon">💳</span>
                  Credit/Debit Card
                </label>
              </div>
              
              <div className="payment-option">
                <input
                  type="radio"
                  id="netbanking"
                  name="paymentMethod"
                  value="netbanking"
                  checked={selectedPaymentMethod === 'netbanking'}
                  onChange={(e) => setSelectedPaymentMethod(e.target.value)}
                />
                <label htmlFor="netbanking">
                  <span className="payment-icon">🏦</span>
                  Net Banking
                </label>
              </div>
              
              <div className="payment-option">
                <input
                  type="radio"
                  id="cod"
                  name="paymentMethod"
                  value="cod"
                  checked={selectedPaymentMethod === 'cod'}
                  onChange={(e) => setSelectedPaymentMethod(e.target.value)}
                />
                <label htmlFor="cod">
                  <span className="payment-icon">💵</span>
                  Cash on Delivery
                </label>
              </div>
            </div>

            {/* Dynamic Payment Details */}
            {renderPaymentDetails()}
          </div>
        </div>

        {/* Order Summary */}
        <div className="payment-right">
          <div className="order-summary">
            <h3>Order Summary</h3>
            <div className="summary-items">
              {cart.items.map((item) => (
                <div key={item.id} className="summary-item">
                  <img src={item.image} alt={item.name} />
                  <div className="item-info">
                    <span className="item-name">{item.name}</span>
                    <span className="item-qty">Qty: {item.quantity}</span>
                  </div>
                  <span className="item-price">₹{(item.price * item.quantity).toLocaleString()}</span>
                </div>
              ))}
            </div>
            
            <div className="price-breakdown">
              <div className="price-row">
                <span>Price ({totalItems} items)</span>
                <span>₹{totalPrice.toLocaleString()}</span>
              </div>
              <div className="price-row">
                <span>Delivery Charges</span>
                <span className="free">FREE</span>
              </div>
              <div className="price-row total">
                <span>Total Amount</span>
                <span>₹{totalPrice.toLocaleString()}</span>
              </div>
            </div>
            
            <button className="pay-button" onClick={handlePayment}>
              Pay ₹{totalPrice.toLocaleString()}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PaymentPage; 