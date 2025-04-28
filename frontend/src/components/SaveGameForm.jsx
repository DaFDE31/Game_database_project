import React, { useState } from 'react';
import './DefaultForm.css';
import PlatformButton from './PlatformButton';
function SaveGameForm({ game, onClose, onSubmit }) {
  const today = new Date().toISOString().split('T')[0];
  const [purchaseDate, setPurchaseDate] = useState(today);
  const [hoursPlayed, setHoursPlayed] = useState(0);
  const [selectedPlatforms, setSelectedPlatforms] = useState([]);

  const handlePlatformToggle = (platform) => {
    setSelectedPlatforms(prev =>
        prev.includes(platform)
            ? prev.filter(p => p !== platform)
            : [...prev, platform]
    );
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
        gameId: game.id,
        purchaseDate: purchaseDate,
        hoursPlayed: hoursPlayed,
        platforms: selectedPlatforms
    });
    onClose();
  };

  return (
    <div className="formOverlay">
      <div className="formContent">
        <h2>Add to Your Library</h2>
        <h3><strong>{game.name}</strong> </h3>
        <p><strong>Release Date:</strong> {game.releaseDate}</p>
        <p><strong>Price:</strong> ${game.price}</p>

        <form onSubmit={handleSubmit}>
          <label>Purchase Date:</label>
          <input 
            type="date" 
            value={purchaseDate} 
            onChange={(e) => setPurchaseDate(e.target.value)} 
          />

          <label>Hours Played:</label>
          <input 
            type="number" 
            value={hoursPlayed} 
            onChange={(e) => setHoursPlayed(e.target.value)} 
            min="0" 
          />

        <div className="platformButtons">
        {game.platforms.slice().sort((a, b) => a.localeCompare(b)).map((plat) => (
            <PlatformButton 
                key={plat}
                title={plat}
                selected={selectedPlatforms.includes(plat)}
                onClick={() => handlePlatformToggle(plat)}
            />
        ))}
        </div>

          <div className="formActions">
            <button type="button" onClick={onClose}>Cancel</button>
            <button type="submit" disabled={selectedPlatforms.length === 0}>Save</button>
          </div>
        </form>
      </div>
    </div>
  );
} export default SaveGameForm