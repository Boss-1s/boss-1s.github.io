// Main function to call notification - try to use this one globally
async function notify(title, //possibly assync, possibly not
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
    };
    
    reg.showNotification(title, config);
}
