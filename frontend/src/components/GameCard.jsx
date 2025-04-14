import React from "react";
import "./GameCard.css";
const GameCard = (game) =>{
    return(
        <div className="playstation">
            <img src="frontend/src/assets/Minecraft.jpg" alt="Game image" />
            <div className="description">
                <h2 className="gameTitle">Devil May Cry V</h2>
            </div>

        </div>
    )
}

export default GameCard