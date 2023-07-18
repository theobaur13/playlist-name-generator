window.open = function(url, windowName, windowFeatures) { 
    console.log('window caught', url, windowName, windowFeatures);
    window.location.href = url;
    return null;
};

document.addEventListener("musickitloaded", async function() {
    const music = MusicKit.getInstance();
    await music.authorize();
    const playlists = await music.api.music('v1/me/library/playlists?include=artwork');
    displayPlaylists(playlists);
});

if (window.MusicKit) {
    document.dispatchEvent(new Event('musickitloaded'));
}

function displayPlaylists(playlists) {
    const playlistContainer = document.getElementById('playlist-container');
    playlistContainer.innerHTML = '';
    
    if (playlists.data.data && playlists.data.data.length > 0) {
        playlists.data.data.forEach(function(playlist) {
            const button = document.createElement('button');
            button.className = 'playlist';
            button.onclick = function() {
                window.location.href = '/playlist/' + playlist.id;
            };

            const imageContainer = document.createElement('div');
            imageContainer.className = 'playlist-image-container';

            const image = document.createElement('img');
            const artwork = playlist.attributes.artwork;

            if (artwork && artwork.url){
                image.src = playlist.attributes.artwork.url;
                image.alt = playlist.attributes.name + ' artwork';
            } else {
                image.src = '/static/img/Apple_Music_Icon_blk_lg_072420.png';
                image.alt = 'Playlist placeholder image';
            }
            image.height = '100';
            image.width = '100';
            image.className = 'playlist-image';

            imageContainer.appendChild(image);

            const playlistName = document.createElement('p');
            playlistName.textContent = playlist.attributes.name;

            button.appendChild(imageContainer);
            button.appendChild(document.createElement('br'));
            button.appendChild(playlistName);

            playlistContainer.appendChild(button);
        });
    } else {
        const message = document.createElement('p');
        message.textContent = 'No playlists found';
        playlistContainer.innerHTML = '';
        playlistContainer.appendChild(message);
    }
}