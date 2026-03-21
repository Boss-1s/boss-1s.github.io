/*
async function notify(title, 
                      body, 
                      icon="/favicon.png", 
                      tag="boss-1s-notif", 
                      actions=[{ action: "open", title: "Open Site" }], 
                      requireInteraction=false, 
                      silent=false
                     ) {
    const sw = await navigator.serviceWorker.ready;
    
    const config = {
        title: title,
        body: body,
        icon: icon,
        tag: tag,
        actions: actions,
        requireInteraction: requireInteraction,
        silent: silent
    }
    
    reg.showNotification(title, config);
}


const opt = {
    body: `Now Playing: ${audioName}`,
    icon: "data:image/jpeg;base64,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",
    tag: "now-playing-notif",
    actions: [
        { action: 'pause', title: 'Pause' },
        { action: 'next', titile: 'Play Next' }
    ],
    requireInteraction: true,
    silent: true,
};
    
*/

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
            const audioName = audios[currentIndex].src.split('/').pop();
            console.log(`Starting song ${audioName}`);
            /*notify("Now Playing",
                   opt[0],
                   opt[1],
                   opt[2],
                   opt[3],
                   opt[4],
                   opt[5],
                  );*/
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
