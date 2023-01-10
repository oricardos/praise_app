import embedVideo from "./embedVideo.js";

export default function voice(){
    const lyrics = document.querySelector('.praise__voice-lyrics');
    if (lyrics){
        const getLyric = document.querySelector('.song-lyric').value;
        const formatLyrics = getLyric.replace(/(\r\n|\r|\n)/g, '<br>');
    
        lyrics.innerHTML = formatLyrics;
    }

    const voiceVideo = document.querySelector('.voices').value;
    const extraVoicesVideo = document.querySelector('.extraVoices').value;
    const youtubeEmbededVoices = document.querySelector('.youtube-embeded-voices');
    const youtubeEmbededExtraVoice = document.querySelector('.youtube-embeded-extra_voice');

    const voiceVideoId = embedVideo(voiceVideo);
    const extraVoicesVideoId = embedVideo(extraVoicesVideo);

    youtubeEmbededVoices.src = `https://www.youtube.com/embed/${voiceVideoId}`;
    youtubeEmbededExtraVoice.src = `https://www.youtube.com/embed/${extraVoicesVideoId}`;
}