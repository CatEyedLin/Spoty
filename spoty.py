import requests

env = open(".env")

client_ID = env.readline().strip("\n")
client_secret = env.readline().strip("\n")

#https://api.spotify.com/v1/me/player/pause
