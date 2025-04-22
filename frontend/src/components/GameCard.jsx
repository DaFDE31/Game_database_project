import React from "react";
import "./GameCard.css";
const GameCard = ({game}) =>{
    return(
        <div className="gameCard">
            {/*<img src="frontend/src/assets/Minecraft.jpg" alt="Game image" />
            
            'id': game.GameID,
                'name': game.Name,
                'price': game.Price,
                'releaseDate': game.ReleaseDate.isoformat(),
                'rating': game.Rating,
                'studio': game.studio.Name if game.studio else 'Unknown',
                'platforms': platform_names
            
            */}
            <h2 className="gameTitle">{game.name}</h2>
            <p>${game.price}</p>
            <p>Released: {game.releaseDate}</p>
            <p>Platforms: {game.platforms.join(", ")}</p>


        </div>
    )
}

export default GameCard