import React from "react";
import "./GameCard.css";
import {Chip, Stack, Typography} from '@mui/material';

        
const SavedCard = ({gameInfo}) =>{
    return(
        <div className="gameCard">
            <h2 className="gameTitle">{gameInfo.name}</h2>
            <p>Hours Played: {gameInfo.hours}</p>
            <Typography variant="body2" color="text.secondary">
                Purchased: {gameInfo.purchaseDate}
            </Typography>
            <Stack direction="row" spacing={1} justifyContent="center" mt={1} flexWrap="wrap">
                {gameInfo.platforms.map((platform, index) => (
                    <Chip key={index} label={platform} variant="outlined" size="small" />
                ))}
            </Stack>
        </div>
    )
}

export default SavedCard