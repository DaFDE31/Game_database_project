 import React from "react"
 import "./PlatformButton.css"
 function PlatformButton({title, selected, onClick}){
    return(
        <button
      className={`platform-button ${title.toLowerCase().replace(/\s/g, '-')} ${selected ? 'selected' : ''}`}
      onClick={onClick}
    >{title}</button>
    )
}export default PlatformButton