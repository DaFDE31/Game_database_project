import React, { useState, useEffect } from 'react';
import PlatformButton from '../components/PlatformButton';
import GameCard from "../components/GameCard"
import "../components/GameCard.css"
import "./GamePage.css"
import SaveGameForm from '../components/SaveGameForm';
import AddGameForm from '../components/AddGameForm';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';

const genericPlatforms = ["All", "PlayStation", "Xbox", "Nintendo", "PC"];



function GamePage() {
  const [showForm, setShowForm] = useState(false);

  const [search, setSearch] = useState("");
  const [showSaveForm, setShowSaveForm] = useState(false);
  const [selectedGame, setSelectedGame] = useState(null);


  const handleAddGame = (newGame) => {
    setGames(prevGames => [...prevGames, newGame])
  };
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
      {filteredGames.map((game) => (
            <GameCard key={game.id} game = {game} onClick={() => {
                if (localStorage.getItem('userName')) {
                  setSelectedGame(game);
                  setShowSaveForm(true);
                }
              }}
            />
        ))}
        <div className="gameCard" onClick={() => setShowForm(true)}>
            <AddCircleOutlineIcon sx={{ fontSize: 60 }} />
        </div>

      {showForm && (
        <AddGameForm
          onClose={() => setShowForm(false)}
          onSubmit={handleAddGame}
        />
      )}

      {showSaveForm && selectedGame && (
        
        <SaveGameForm 
          game={selectedGame} 
          onClose={() => setShowSaveForm(false)} 
          onSubmit={async (playData) => {

            const fullData = {
              ...playData,
              userName: localStorage.getItem('userName')
            };

            try {
              const response = await fetch('http://localhost:5001/api/save_play', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(fullData)
              });
              if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.error}`);
              }
            } catch (error) {
              console.error('Error saving play record:', error);
            }
          }}
          
        />
      )}

      </div>
        
      
    </div>
  );
}

export default GamePage;