from flask import Flask, request, jsonify
from helper_functions import generate_playlist

app = Flask(__name__)

@app.route('/playlistgenerator', methods=['POST'])
def build_playlist():

    ## We're assuming POST with application/json content type

    ## Get the title from the request
    playlist_title = request.json['title']

    ## Get the tracks
    tracks = request.json['tracks']

    ## Generate the playlist
    playlist_link = generate_playlist(playlist_title, tracks)

    return jsonify(
        link = playlist_link
    )

if __name__ == '__main__':
    app.run(host='localhost', debug=True)