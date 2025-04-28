import React, { useState } from 'react';
import './DefaultForm.css';

function RegisterForm({ onClose }) {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
    firstName: '',
    lastName: '',
    region: '',
    dob: '',
  });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5001/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await response.json();

      if (!response.ok) {
        setError(data.error || 'Registration failed');
        return;
      }

      localStorage.setItem('userName', data.userName || formData.username); 
      onClose();
      window.location.reload();

    } catch (err) {
      setError('Registration failed. Please try again.');
    }
  };

  return (
    <div className="formOverlay">
      <div className="formContent">
        <h2>Register</h2>
        <form onSubmit={handleRegister}>
          <input name="username" placeholder="Username" value={formData.username} onChange={handleChange} required />
          <input name="password" type="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
          <input name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
          <input name="firstName" placeholder="First Name" value={formData.firstName} onChange={handleChange} required/>
          <input name="lastName" placeholder="Last Name" value={formData.lastName} onChange={handleChange} required/>
          <input name="region" placeholder="Region" value={formData.region} onChange={handleChange} />
          <label name = "dob">Date of Birth</label>
          <input name="dob" type="date" placeholder="Date of Birth" value={formData.dob} onChange={handleChange} required/>

          {error && <div style={{ color: 'red' }}>{error}</div>}
          <div className="formActions">
            <button type="button" onClick={onClose}>Cancel</button>
            <button type="submit">Register</button>
          </div>
        </form>
      </div>
    </div>
  );
}
export default RegisterForm