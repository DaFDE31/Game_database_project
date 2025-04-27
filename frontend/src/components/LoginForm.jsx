import React, { useEffect, useState } from "react";
import "./DefaultForm.css";

function LoginForm({ onClose , switchToRegister}) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5001/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });
      const data = await response.json();
      
      if (!response.ok) {
        setError(data.error || 'Login failed');
        return;
      }

      localStorage.setItem('userName', data.userName);
      alert('Login successful!');
      onClose();
    } catch (err) {
      setError('Login failed. Please try again.');
    }
  };

  return (
    <div className="formOverlay">
      <div className="formContent">
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <input
            className="formInput"
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <input
            className="formInput"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <div className="formActions">
            <button type="button" onClick={onClose}>Cancel</button>
            <button onClick={switchToRegister}>New User? Register here</button>
            <button type="submit">Login</button>
          </div>
        </form>
      </div>
    </div>
  );
}
export default LoginForm