self.addEventListener('notificationclick', function(event) {
    event.notification.close();

    if (event.action === 'pause') {
        console.log("pausing song");
    } else if (event.action === 'resume') {
        console.log("resuming song");
    } else if (event.action === 'next') {
        console.log("skipping to next song")
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
