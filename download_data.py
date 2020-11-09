#Download data from youtube using pytube
#this is just a script to download playlist (worked on py3.8.6)
#------------
#NOTE: please make sure your list doesn't have any private or deleted videos
#
#url = playlist-url
#path = dir-to-save
#
#this download script go with convert_to_wav.py but this script sometimes error
#so i make 2 script
#---------------

from pytube import YouTube
from pytube import Playlist
import re
import pytube
import os

def download_playlist(url, path_dir):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    #prints each video url, which is the same as iterating through playlist.video_urls
    for url in playlist:
        print(url)
        YouTube(url).streams.filter(only_audio=True).first().download("/Users/trongthanht3/PycharmProjects/text2speech/data")
        print('download complete!')
        print("----------------------")

def download_playlist_video(_url, path_dir):
    playlist = Playlist(_url)
    #playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    #prints each video url, which is the same as iterating through playlist.video_urls
    for url in playlist:
        print(url)
        #only_audio=false mean we down both audio and video
        YouTube(url).streams.filter(only_audio=False).first().download(path_dir)
        print('download complete!')
        print("----------------------")

url = 'https://www.youtube.com/playlist?list=PLfKmBpK2q_5NaYBg_BI6-ccXJDjSWe7Zc'
path = '/Users/thanh/WorkAca/ZaloTeam/data'
download_playlist_video(url, path)
# download_playlist(url, path)
# pl = Playlist(url)
# pl.download_all(path)