#importing our libraries
import json
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_creds = SpotifyClientCredentials("client_id","client_secret_key") #my spotify credentials
sp = spotipy.Spotify(client_credentials_manager=client_creds) #spotify object

def get_track_id(playlist_id): #method to get the track id from playlist id
  music_id_list = []
  playlist = sp.playlist(playlist_id)
  for items in playlist['tracks']['items']:
    music_track = items['track']
    music_id_list.append(music_track['id'])
  return music_id_list

def get_track_data(track_id): #method that takes in single track id as input and returns the related data points
  meta = sp.track(track_id)
  track_details = {"name":meta['name'],"artist":meta['album']['artists'][0]['name']}
  return track_details

playlist_id = input('Enter the playlist ID: ') #taking the input of the playlist id
track_ids = get_track_id(playlist_id=playlist_id) #getting the track ids
print(len(track_ids)) #printing the length of the track ids
print(track_ids) #printing the track ids

tracks = [] #empty list to store our track details
for i in range(len(track_ids)):
  time.sleep(.5) #this makes a little bit of delay before fetching the data between two tracks as we might get blocked if we give hit spotify too many times
  track = get_track_data(track_ids[i])
  tracks.append(track)

with open('disgust_songs.json','w') as outfile: #writing our output to a json file
  json.dump(tracks,outfile,indent=4)
