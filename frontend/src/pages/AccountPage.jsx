import React, { useEffect, useState } from "react";
import "./AccountPage.css";

function AccountPage() {
  const [userInfo, setUserInfo] = useState(null);

  useEffect(() => {
    const fetchUserInfo = async () => {
      const userName = localStorage.getItem('userName');
      if (!userName) return;

      try {
        const response = await fetch('http://localhost:5001/api/user_info', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ userName }),
        });
        const data = await response.json();
        setUserInfo(data);
      } catch (error) {
        console.error('Failed to fetch user info:', error);
      }
    };

    fetchUserInfo();
  }, []);

  if (!userInfo) {
    return <div>Loading account information...</div>;
  }

  return (
    <div className="accountPage">
      <h1>My Account</h1>
      <div className="accountInfo">
        <p><strong>First Name:</strong> {userInfo.firstName}</p>
        <p><strong>Last Name:</strong> {userInfo.lastName}</p>
        <p><strong>Username:</strong> {userInfo.userName}</p>
        <p><strong>Date of Birth:</strong> {userInfo.dob}</p>
        <p><strong>Region:</strong> {userInfo.region}</p>
      </div>
    </div>
  );
}

export default AccountPage;
