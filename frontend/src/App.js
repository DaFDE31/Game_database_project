import {BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import GamePage from './pages/GamePage';
import SavedGamesPage from './pages/SavedGamesPage';
import AccountPage from './pages/AccountPage';
import { useState } from 'react';
import RegisterForm from './components/RegisterForm';
import LoginForm from './components/LoginForm';
import "./App.css"


function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const isLoggedIn = !!localStorage.getItem('userName');

  const switchToRegister = () =>{
    setShowLogin(false);
    setShowRegister(true);
  };
  const handleLogout = () => {
    localStorage.removeItem('userName');
    window.location.href = '/';
  };

  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <div className="nav-links">
            <Link to="/" className="link">Games</Link>
            {isLoggedIn && (
              <>
                <Link to="/saved" className="link">Saved Games</Link>
                <Link to="/account" className="link">Account</Link>
              </>
            )}
          </div>

          <div className="auth-buttons">
            {isLoggedIn ? (
              <button className="link" onClick={handleLogout}>Logout</button>
            ) : (
              <>
                <button className="link" onClick={() => setShowLogin(true)}>Login</button>
                <button className="link" onClick={() => setShowRegister(true)}>Register</button>
              </>
            )}
          </div>
        </nav>
        {showLogin && (
        <LoginForm onClose={() => setShowLogin(false)} switchToRegister = {switchToRegister}/>
      )}
      
      {showRegister && (
        <RegisterForm onClose={() => setShowRegister(false)} />
      )}

        <Routes>
          <Route path="/" element={<GamePage />} />
          <Route path="/saved" element={<SavedGamesPage />} />
          <Route path="/account" element={<AccountPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
