import React, { useEffect, useState } from "react";
import "./DefaultForm.css";

function AddGameForm({ onClose, onSubmit }) {
  const [formData, setFormData] = useState({
    name: "",
    price: "",
    releaseDate: "",
    studio: "",
    platforms: [],
  });

  const [platforms, setPlatforms] = useState([]);
  const [studios, setStudios] = useState([]);

  useEffect(() => {
    const fetchPlatforms = async () => {
      const response = await fetch('http://localhost:5001/api/platforms');
      const data = await response.json();
      setPlatforms(data);
    };

    const fetchStudios = async () => {
      const response = await fetch('http://localhost:5001/api/studios');
      const data = await response.json();
      setStudios(data);
    };

    fetchPlatforms();
    fetchStudios();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handlePlatformsChange = (e) => {
    const selected = Array.from(e.target.selectedOptions).map(option => option.value);
    setFormData((prev) => ({ ...prev, platforms: selected }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    try {
      const response = await fetch('http://localhost:5001/api/games', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      });
  
      if (!response.ok) {
        throw new Error('Failed to add game');
      }
  
      const data = await response.json();
  
      console.log('Game added successfully:', data);
  
      const newGame = { ...formData, id: data.gameID};
  
      onSubmit(newGame);
      onClose();
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };
  

  return (
    <div className="formOverlay">
      <div className="formContent">
        <h2>Add New Game</h2>
        <form onSubmit={handleSubmit}>
          <input
            name="name"
            placeholder="Game Name"
            value={formData.name}
            onChange={handleChange}
            required
          />
          <input
            name="price"
            placeholder="Price"
            type="number"
            value={formData.price}
            onChange={handleChange}
            required
          />
          <input
            name="releaseDate"
            placeholder="Release Date"
            type="date"
            value={formData.releaseDate}
            onChange={handleChange}
            required
          />

          <select
            name="studio"
            value={formData.studio}
            onChange={handleChange}
          >
            <option value="">Select Studio</option>
            {studios.map((studio) => (
              <option key={studio.id} value={studio.name}>
                {studio.name}
              </option>
            ))}
          </select>

          <select
            multiple
            value={formData.platforms}
            onChange={handlePlatformsChange}
            required
          >
            {platforms.map((platform) => (
              <option key={platform.id} value={platform.name}>
                {platform.name}
              </option>
            ))}
          </select>

          <div className="formActions">
            <button type="button" onClick={onClose}>Cancel</button>
            <button type="submit">Add Game</button>
          </div>
        </form>
      </div>
    </div>
  );
}
export default AddGameForm