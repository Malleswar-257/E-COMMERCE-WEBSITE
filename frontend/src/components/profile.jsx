import React, { useState } from 'react';
import { Container, Row, Col, Card, Button, Form } from 'react-bootstrap';

const Profile = () => {
  const [editing, setEditing] = useState(false);
  const [user, setUser] = useState({
    name: 'Malli',
    email: 'malleswar@gmail.com',
    phone: '+91 xxxxxxxx88',
    avatar: "src/assets/admin.png",
    address: '123, MG Road, Hyderabad, India',
  });

  const [formData, setFormData] = useState({ ...user });

  const handleEditToggle = () => {
    setEditing(!editing);
    setFormData({ ...user });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSave = () => {
    setUser({ ...formData });
    setEditing(false);
  };

  return (
    <Container style={{ paddingTop: '40px', paddingBottom: '40px' }}>
      <Row className="g-4">
        {/* Left Panel: Avatar + Basic Info */}
        <Col lg={4} md={5} sm={12}>
          <Card style={{ borderRadius: '20px', boxShadow: '0 0 15px rgba(0,0,0,0.1)' }}>
            <Card.Body className="text-center" style={{ padding: '30px' }}>
              <img
                src="src/assets/admin.png"
                alt="User"
                style={{
                  width: '120px',
                  height: '120px',
                  borderRadius: '50%',
                  objectFit: 'cover',
                  marginBottom: '15px',
                  boxShadow: '0 4px 8px rgba(0,0,0,0.2)'
                }}
              />
              <h4 style={{ fontWeight: 600 }}>{user.name}</h4>
              <p style={{ color: '#777' }}>{user.email}</p>
              <Button
                variant={editing ? 'secondary' : 'primary'}
                onClick={handleEditToggle}
                style={{ marginTop: '10px', padding: '6px 16px', borderRadius: '30px' }}
              >
                {editing ? 'Cancel' : 'Edit Profile'}
              </Button>
            </Card.Body>
          </Card>
        </Col>

        {/* Right Panel: Info Form + Orders */}
        <Col lg={8} md={7} sm={12}>
          <Card style={{ borderRadius: '20px', padding: '30px', boxShadow: '0 0 15px rgba(0,0,0,0.05)' }}>
            <h5 style={{ fontWeight: '600', marginBottom: '20px' }}>
              {editing ? 'Edit Your Information' : 'Profile Information'}
            </h5>
            <Form>
              <Row className="mb-3">
                <Col sm={6}>
                  <Form.Label>Full Name</Form.Label>
                  <Form.Control
                    type="text"
                    name="name"
                    value={formData.name}
                    disabled={!editing}
                    onChange={handleChange}
                    style={{ borderRadius: '10px' }}
                  />
                </Col>
                <Col sm={6}>
                  <Form.Label>Email</Form.Label>
                  <Form.Control
                    type="email"
                    name="email"
                    value={formData.email}
                    disabled={!editing}
                    onChange={handleChange}
                    style={{ borderRadius: '10px' }}
                  />
                </Col>
              </Row>

              <Row className="mb-3">
                <Col sm={6}>
                  <Form.Label>Phone Number</Form.Label>
                  <Form.Control
                    type="text"
                    name="phone"
                    value={formData.phone}
                    disabled={!editing}
                    onChange={handleChange}
                    style={{ borderRadius: '10px' }}
                  />
                </Col>
                <Col sm={6}>
                  <Form.Label>Address</Form.Label>
                  <Form.Control
                    type="text"
                    name="address"
                    value={formData.address}
                    disabled={!editing}
                    onChange={handleChange}
                    style={{ borderRadius: '10px' }}
                  />
                </Col>
              </Row>

              {editing && (
                <Button
                  variant="success"
                  onClick={handleSave}
                  style={{ borderRadius: '25px', padding: '8px 20px' }}
                >
                  Save Changes
                </Button>
              )}
            </Form>
          </Card>

          {/* Recent Orders */}
          <Card
            style={{
              borderRadius: '20px',
              marginTop: '30px',
              padding: '25px',
              boxShadow: '0 0 15px rgba(0,0,0,0.05)'
            }}
          >
            <h5 style={{ fontWeight: 600, marginBottom: '20px' }}>Recent Orders</h5>
            <ul className="list-group list-group-flush">
              <li className="list-group-item d-flex justify-content-between align-items-center">
                <span>Order #12345</span>
                <span className="text-success">Delivered</span>
              </li>
              <li className="list-group-item d-flex justify-content-between align-items-center">
                <span>Order #12346</span>
                <span className="text-warning">In Transit</span>
              </li>
              <li className="list-group-item d-flex justify-content-between align-items-center">
                <span>Order #12347</span>
                <span className="text-danger">Cancelled</span>
              </li>
            </ul>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Profile;
