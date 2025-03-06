// Disables web gl features on the page if the browser does not support it
function disableWebGLFeatures() {
    const gl = document.createElement('canvas').getContext('webgl2');
    if (!gl) {
        let gameContainer = document.getElementById("game-container");
        gameContainer.innerText = "WebGL2 is not supported by your browser. Try this page out in Chrome or Firefox to play this game.";
    } else {
        let gameLink = document.getElementById("game-link");
        gameLink.hidden = false;
    }
}


export default disableWebGLFeatures;

// Sets year in copyright footer to the proper year.
document.getElementById("year").innerHTML = new Date().getFullYear();
