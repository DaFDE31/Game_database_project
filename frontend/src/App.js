import React, { useState, useEffect } from 'react';
import PlatformButton from './components/PlatformButton';

// Sample data
/*const games = [
  { id: 1, name: 'God of War', platforms: ['PlayStation', "Steam/PC"] },
  { id: 2, name: 'Halo Infinite', platforms: ['Xbox'] },
  { id: 3, name: 'The Legend of Zelda: Breath of the Wild', platforms: ['Nintendo'] },
  { id: 4, name: 'Forza Horizon 5', platforms: ['Xbox'] },
  { id: 5, name: 'Cyberpunk 2077', platforms: ["PlayStation", "Xbox", 'PC'] },
  { id: 6, name: 'Spider-Man 2', platforms: ['Playstation', "PC"] },
];*/
const genericPlatforms = ["All", "PlayStation", "Xbox", "Nintendo", "PC"];


function App() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    const fetchGames = async () => {
      try {
        const response = await fetch('http://localhost:5001/api/games');
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

  const filteredGames = selectedPlatform === 'All'
  ? games
  : games.filter((game) =>
      game.platforms.some((platform) =>
        platform.includes(selectedPlatform)
      )
    );

  return (
    <div className="App" style={{ fontFamily: 'sans-serif', padding: '20px' }}>
      <h1>Gaming Database</h1>
      <nav style={{ marginBottom: '20px' }}>
        {genericPlatforms.map((genericPlatform) =>(
          <PlatformButton title = {genericPlatform} selected = {selectedPlatform === genericPlatform} onClick = {() =>handleFilter(genericPlatform)}/>
        ))}
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
