import spotipy
from dotenv import dotenv_values
config = dotenv_values(".env")
MY_CLIENT_ID = config["MY_CLIENT_ID"]
MY_CLIENT_SECRET = config["MY_CLIENT_SECRET"]
MY_USER_NAME = config["MY_USER_NAME"]

def generate_playlist(name, tracks):
    """
    Generates a playlist with the given name
    and a list of spotify track urls
    name: string name of the playlist
    tracks: list list of spotify track urls
    """

    
    token = spotipy.util.prompt_for_user_token(
        username=MY_USER_NAME,
        scope='playlist-modify-public',
        client_id=MY_CLIENT_ID,
        client_secret=MY_CLIENT_SECRET,
        redirect_uri="http://localhost:8888/callback"
    )

    ## Create an instance of the client
    sp = spotipy.Spotify(auth=token)

    # sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=MY_CLIENT_ID, client_secret=MY_CLIENT_SECRET))

    ## Get my User ID
    id = sp.current_user()['id']

    ## Create the playlist
    pl_obj = sp.user_playlist_create(id, name)

    ## Get the playlist id
    pl_id = pl_obj['id']

    ## Add the tracks
    sp.user_playlist_add_tracks(id, pl_id, tracks)

    return pl_obj['external_urls']['spotify']