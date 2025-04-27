import React, { useState, useEffect } from 'react';
import PlatformButton from '../components/PlatformButton';
import GameCard from "../components/GameCard" //Gonna use a different GameCard that will be made later
import "../components/GameCard.css"
import "./GamePage.css"

const genericPlatforms = ["All", "PlayStation", "Xbox", "Nintendo", "PC"];



function SavedGamesPage() {

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
    <div className="gamePage">
      <h1>Gaming Database</h1>
      <nav style={{ marginBottom: '20px' }}>
        {genericPlatforms.map((genericPlatform) =>(
          <PlatformButton key = {genericPlatform} title = {genericPlatform} selected = {selectedPlatform === genericPlatform} onClick = {() =>handleFilter(genericPlatform)}/>
        ))}
      </nav>
      <div className='gameSection'>
      {filteredGames.map((game) => (
            <GameCard key={game.id} game = {game}/>
        ))}
      </div>
    </div>
  );
}

export default SavedGamesPage;