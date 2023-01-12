import embedVideo from "./embedVideo.js";

export default function instrumental(){
    const instrumentalPage = document.querySelector('.instrumental-page');

    if (instrumentalPage) {
        //captura dos valores
        const acousticGuitar = document.querySelector('.acoustic_guitar').value;
        const electricGuitar = document.querySelector('.electric_guitar').value;
        const keyboard = document.querySelector('.keyboard').value;
        const bass = document.querySelector('.bass').value;
        const drums = document.querySelector('.drums').value;

        //captura dos iframes
        const youtubeEmbedesAcousticGuitar = document.querySelector('.youtube-embeded-acoustic_guitar');
        const youtubeEmbedesElectricGuitar = document.querySelector('.youtube-embeded-electric_guitar');
        const youtubeEmbedesKeyboard = document.querySelector('.youtube-embeded-keyboard');
        const youtubeEmbedesBass = document.querySelector('.youtube-embeded-bass');
        const youtubeEmbedesDrums = document.querySelector('.youtube-embeded-drums');

        //extraindo id dos videos 
        const acousticGuitarId = embedVideo(acousticGuitar);
        const electricGuitarId = embedVideo(electricGuitar);
        const keyboardId = embedVideo(keyboard);
        const bassId = embedVideo(bass);
        const drumsId = embedVideo(drums);

        //embedando src
        youtubeEmbedesAcousticGuitar.src = `https://www.youtube.com/embed/${acousticGuitarId}`;
        youtubeEmbedesElectricGuitar.src = `https://www.youtube.com/embed/${electricGuitarId}`;
        youtubeEmbedesKeyboard.src = `https://www.youtube.com/embed/${keyboardId}`;
        youtubeEmbedesBass.src = `https://www.youtube.com/embed/${bassId}`;
        youtubeEmbedesDrums.src = `https://www.youtube.com/embed/${drumsId}`;
    }
}