import React, { useState, useEffect } from 'react';

/*// Sample data
const games = [
  { id: 1, title: 'God of War', platform: ['Playstation', "PC"] },
  { id: 2, title: 'Halo Infinite', platform: ['Xbox'] },
  { id: 3, title: 'The Legend of Zelda: Breath of the Wild', platform: ['Nintendo'] },
  { id: 4, title: 'Forza Horizon 5', platform: ['Xbox'] },
  { id: 5, title: 'Cyberpunk 2077', platform: ["Playstation", "Xbox", 'PC'] },
  { id: 6, title: 'Spider-Man 2', platform: ['Playstation', "PC"] },
];
*/

function App() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/games');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setGames(data);
      } catch (err) {
        console.error('Error fetching games:', err);
      }
    };

    fetchGames();
  }, []);

  const [selectedPlatform, setSelectedPlatform] = useState('All');

  const handleFilter = (platform) => {
    setSelectedPlatform(platform);
  };

  const filteredGames = selectedPlatform === 'All' ? games : games.filter((game) => game.platforms.includes(selectedPlatform));

  return (
    <div className="App" style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h1>Gaming Database</h1>
      <nav style={{ marginBottom: '20px' }}>
        <button onClick={() => handleFilter('All')} style={{ marginRight: '10px' }}>All</button>
        <button onClick={() => handleFilter('Playstation')} style={{ marginRight: '10px' }}>Playstation</button>
        <button onClick={() => handleFilter('Xbox')} style={{ marginRight: '10px' }}>Xbox</button>
        <button onClick={() => handleFilter('PC')} style={{ marginRight: '10px' }}>PC</button>
        <button onClick={() => handleFilter('Nintendo')} style={{ marginRight: '10px' }}>Nintendo</button>
      </nav>

      <ul>
        {filteredGames.map((game) => (
          <li key={game.id}>{game.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
