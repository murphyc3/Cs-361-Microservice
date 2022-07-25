# Spotify Playlist Creator Microservice

Note that the user **must connect to OSU VPN** in order to navigate to the URL to use the microservice.

### How To Request Data
As stated above, make sure you are connected to the VPN.

In order to create a playlist the user must send a POST request to the following URL:
[http://flip1.engr.oregonstate.edu:3138/playlistgenerator](http://flip1.engr.oregonstate.edu:3138/playlistgenerator).

The POST request must submit JSON data. So, it must have its mimetype set to be application/json. The JSON object that
is submitted must be formatted as follows:

```
{
    "title": "Insert Playlist Title Here",
    "tracks": [
        "Spotify URL to song 1",
        "Spotify URL to song 2",
        "Spotify URL to song 3"
    ]
}
```

You can submit any many track URLs as you like, there is no limit. Here is some example code
for submitting a POST request using Python's `requests` package:

```
import requests

request = requests.post('http://flip1.engr.oregonstate.edu:3138/playlistgenerator', json={
    'title': "My playlist", 
    'tracks': [
        "https://open.spotify.com/track/2NtqZmfRIDkXJ2YvY2Kv1F?si=c286783f05554217",
        "https://open.spotify.com/track/4lFO4X6ef61SR6M1KXkSRN?si=55590f077b4a410e",
        "https://open.spotify.com/track/4pCNJwixy2ImFncaPY2yE2?si=7b57e427de78428c"
        ]
    })
```

### How To Receive Data
Once the playlist is created the service sends a Response object to the user that is a JSON object,
thus its mimtype is application/json. The format of the returned JSON is as follows:

```
{
    "link": "URL To The Created Spotify Playlist"
}
```

If you were to use the `requests` package in Python to make your request, you can access the JSON object in
the response as follows:

```
import requests

## Make a request at the link with a valid JSON object
response = requests.post('http://flip1.engr.oregonstate.edu:3138/playlistgenerator', json={
    'title': "My playlist", 
    'tracks': [
        "https://open.spotify.com/track/2NtqZmfRIDkXJ2YvY2Kv1F?si=c286783f05554217",
        "https://open.spotify.com/track/4lFO4X6ef61SR6M1KXkSRN?si=55590f077b4a410e",
        "https://open.spotify.com/track/4pCNJwixy2ImFncaPY2yE2?si=7b57e427de78428c"
        ]
    })

## Get JSON response
json_response = response.json()

## Get the url
url = json_response['link']
```