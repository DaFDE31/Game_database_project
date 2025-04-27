import React from "react";
import "./GameCard.css";
import {Chip, Stack, Typography} from '@mui/material';

        
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
            <Typography variant="body2" color="text.secondary">
                Released: {game.releaseDate}
            </Typography>
            <Stack direction="row" spacing={1} justifyContent="center" mt={1} flexWrap="wrap">
                {game.platforms.map((platform, index) => (
                    <Chip key={index} label={platform} variant="outlined" size="small" />
                ))}
            </Stack>
        </div>
    )
}

export default GameCard