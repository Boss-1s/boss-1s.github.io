document.addEventListener('play', function(e) {
    const audios = document.getElementsByTagName('audio');
    for (let i = 0; i < audios.length; i++) {
        if (audios[i] != e.target) {
            audios[i].pause();
            audios[i].currentTime = 0;
        }
    }
}, true);

document.getElementById('play-all').addEventListener('click', function() {
    alert("this will play all songs on the order they appear on this page.\nto skip a song, click the next button.\nI will add shuffling and looping later.");
    
    const audios = document.getElementsByTagName("audio");
    let currentIndex = 0;
    
    function playNext() {
        if (currentIndex < audios.length) {
            console.log(`Starting song ${audios[currentIndex]}`);
            audios[currentIndex].play();
            audios[currentIndex].onended = () => {
                audios[currentIndex].currentTime = 0;
                setTimeout(() => {
                    currentIndex++;
                    playNext();
                }, 1000);
            };
        } else {
            if (document.getElementById('loop').checked) {
                currentIndex = 0;
                playNext();
            }
    }

    // Start the sequence
    playNext();
});


document.getElementById('play-next').addEventListener('click', function() {
    // 1. Get all audio elements on the page
    const audios = Array.from(document.querySelectorAll('audio'));
    
    // 2. Find the index of the currently playing audio
    const currentIndex = audios.findIndex(audio => !audio.paused);

    // 3. If an audio is playing, stop it and play the next one
    if (currentIndex !== -1) {
      audios[currentIndex].pause();
      audios[currentIndex].currentTime = 0; // Optional: Reset track to start

      // Calculate next index (loops back to start if at the end)
      const nextIndex = (currentIndex + 1) % audios.length;
      audios[nextIndex].play();
    } else {
      // Optional: If nothing is playing, start the first one
      audios[0].play();
    }
});

document.getElementById('pause').addEventListener('click', function() {
    const audios = Array.from(document.querySelectorAll('audio'));
    const currentIndex = audios.findIndex(audio => !audio.paused);
    if (currentIndex !== -1) {
      audios[currentIndex].pause();
    }
});

document.getElementById('resume').addEventListener('click', function() {
    const audios = Array.from(document.querySelectorAll('audio'));
    const currentIndex = audios.findIndex(audio => audio.paused && !audio.ended && audio.currentTime > 0);
    if (currentIndex !== -1) {
      audios[currentIndex].play();
    }
});
