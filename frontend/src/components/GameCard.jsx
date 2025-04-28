import React from "react";
import "./GameCard.css";
import {Chip, Stack, Typography} from '@mui/material';

        
const GameCard = ({game, onClick}) =>{
    return(
        <div className="gameCard" onClick={onClick}>
            <h2 className="gameTitle">{game.name}</h2>
            <p>{game.price === 0 ? "Free" : `$${game.price}`}</p>
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