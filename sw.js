self.addEventListener('notificationclick', function(event) {
    event.notification.close();

    if (event.action === 'pause') {
        console.log("pausing song");
        document.getElementById('pause').click()
        const old = event.notification;
        const newConfig = {
            body: old.body,
            icon: old.icon,
            tag: old.tag,
            requireInteraction: true,
            silent: true,
            actions: [
                {action: 'resume', title: 'Resume'},
                {action: 'next', title: 'Play Next'},
            ],
        };
        self.registration.showNotification(old.title, newConfig);
    } else if (event.action === 'resume') {
        console.log("resuming song");
        document.getElementById('resume').click();
        const old = event.notification;
        const newConfig = {
            body: old.body,
            icon: old.icon,
            tag: old.tag,
            requireInteraction: true,
            silent: true,
            actions: [
                {action: 'pause', title: 'Pause'},
                {action: 'next', title: 'Play Next'},
            ],
        };
        self.registration.showNotification(old.title, newConfig);
    } else if (event.action === 'next') {
        console.log("skipping to next song");
        document.getElementById('play-next').click();
    } else {
        // Look for existing windows and focus if found
        event.waitUntil(
            clients.matchAll({ type: 'window', includeUncontrolled: true })
                .then(windowClients => {
                for (var i = 0; i < windowClients.length; i++) {
                    var client = windowClients[i];
                    // Check for specific URL or just the first available client
                    if (client.url === '/' && 'focus' in client) {
                        return client.focus();
                    }
                }
                // If no tab is found, open a new one
                if (clients.openWindow) {
                    return clients.openWindow('/');
                }
            })
        );
    }
});
