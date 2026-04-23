document.addEventListener('play', function(e) {
    const audios = document.getElementsByTagName('audio');
    for (let i = 0; i < audios.length; i++) {
        if (audios[i] != e.target) {
            audios[i].pause();
        }
    }
}, true);

document.getElementById('play-all').addEventListener('click', function() {
    const audios = document.getElementsByTagName("audio");
    let currentIndex = 0;
    
    function playNext() {
        if (currentIndex < audios.length) {
            audios[currentIndex].play();
            audios[currentIndex].onended = () => {
                currentIndex++;
                playNext();
            };
        }
    }

    // Start the sequence
    playNext();
