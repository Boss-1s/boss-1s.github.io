document.addEventListener('play', function(e) {
    const audios = document.getElementsByTagName('audio');
    for (let i = 0; i < audios.length; i++) {
        if (audios[i] != e.target) {
            audios[i].pause();
        }
    }
}, true);
