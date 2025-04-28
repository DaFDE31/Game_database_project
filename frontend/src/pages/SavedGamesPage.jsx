import React, { useState, useEffect } from 'react';
import PlatformButton from '../components/PlatformButton';
import SavedCard from '../components/SavedCard';
import "../components/GameCard.css"
import "./GamePage.css"

const genericPlatforms = ["All", "PlayStation", "Xbox", "Nintendo", "PC"];



function SavedGamesPage() {

  const [search, setSearch] = useState("");

   const [games, setGames] = useState([]);

   useEffect(() => {
    const fetchSavedGames = async () => {
      try {
        const response = await fetch('http://localhost:5001/api/saved_games', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ userName: localStorage.getItem('userName') })
        });
  
        const data = await response.json();
        setGames(data);
      } catch (error) {
        console.error('Error fetching saved games:', error);
      }
    };
  
    fetchSavedGames();
  }, []);
  

  const [selectedPlatform, setSelectedPlatform] = useState('All');

  const handleFilter = (platform) => {
    setSelectedPlatform(platform);
  };

  const filteredGames = games.filter((game) => {
    const platformfilter = selectedPlatform === 'All' ||
      game.platforms.some((platform) =>
        platform.includes(selectedPlatform)
      )

      const searchfiler = search === "" || game.name.toLowerCase().includes(search.toLowerCase());
      return platformfilter && searchfiler;
  });

  return (
    <div className="gamePage">
      <h1>Gaming Database</h1>
      <nav style={{ marginBottom: '20px' }}>
        {genericPlatforms.map((genericPlatform) =>(
          <PlatformButton key = {genericPlatform} title = {genericPlatform} selected = {selectedPlatform === genericPlatform} onClick = {() =>handleFilter(genericPlatform)}/>
        ))}
        
      </nav>
      <input type="text" name="search" id="search" placeholder='SearchBar' value={search} onChange={(e) => setSearch(e.target.value)}/>
      <div className='gameSection'>
      {filteredGames.map((gameInfo) => (
        <SavedCard key={gameInfo.name} gameInfo={gameInfo} />
        ))}
      </div>
    </div>
  );
}

export default SavedGamesPage;