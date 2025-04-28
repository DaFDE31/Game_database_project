import React from "react";
import "./GameCard.css";
import {Chip, Stack, Typography} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
        
const SavedCard = ({gameInfo, onDelete}) =>{
    return(
        <div className="gameCard" style = {{position: "relative"}}>
            <CloseIcon className="closebutton" onClick = {() =>onDelete(gameInfo)}/>
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