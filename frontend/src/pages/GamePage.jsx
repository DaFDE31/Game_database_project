import React, { useState, useEffect } from 'react';
import PlatformButton from '../components/PlatformButton';
import GameCard from "../components/GameCard"
import "../components/GameCard.css"
import "./GamePage.css"
import AddGameForm from '../components/AddGameForm';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
// Sample data
/*const games = [
  { 
    id: 1, 
    name: 'God of War', 
    platforms: ['PlayStation', 'Steam/PC'], 
    releaseDate: '2018-04-20', 
    price: 39.99 
  },
  { 
    id: 2, 
    name: 'Halo Infinite', 
    platforms: ['Xbox'], 
    releaseDate: '2021-12-08', 
    price: 59.99 
  },
  { 
    id: 3, 
    name: 'The Legend of Zelda: Breath of the Wild', 
    platforms: ['Nintendo'], 
    releaseDate: '2017-03-03', 
    price: 59.99 
  },
  { 
    id: 4, 
    name: 'Forza Horizon 5', 
    platforms: ['Xbox'], 
    releaseDate: '2021-11-09', 
    price: 59.99 
  },
  { 
    id: 5, 
    name: 'Cyberpunk 2077', 
    platforms: ['PlayStation', 'Xbox', 'Steam/PC'], 
    releaseDate: '2020-12-10', 
    price: 29.99 
  },
  { 
    id: 6, 
    name: 'Spider-Man 2', 
    platforms: ['PlayStation', 'Steam/PC'], 
    releaseDate: '2023-10-20', 
    price: 69.99 
  }
];*/

const genericPlatforms = ["All", "PlayStation", "Xbox", "Nintendo", "PC"];



function GamePage() {
  const [showForm, setShowForm] = useState(false);

  const [search, setSearch] = useState("");

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
            <GameCard key={game.id} game = {game}/>
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
      </div>
        
      
    </div>
  );
}

export default GamePage;