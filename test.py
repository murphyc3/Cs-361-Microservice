import requests

res = requests.post('http://localhost:5000/playlistgenerator', json={
    'title': "playlist_title", 
    'tracks': ["https://open.spotify.com/track/2NtqZmfRIDkXJ2YvY2Kv1F?si=c286783f05554217"]
    })

print(res.json())