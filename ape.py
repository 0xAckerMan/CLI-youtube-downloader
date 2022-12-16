#!/usr/bin/python3
# Author: @K0r3s

import argparse
from pytube import YouTube

# The path to where the video and audio will be saved
AUD_DIR = './audios'
VID_DIR = './videos'

# The audio function
def Audio(video_url):
    aud = YouTube(video_url)
    audio = aud.streams.filter(only_audio = True).first()

    try:
        audio.download(AUD_DIR)
    except:
        print("Audio failed to be downloaded")

    print("Audio ha been successfully downloaded")


# The video function
def Video(video_url):
    video = YouTube(video_url)
    video = video.streams.get_hightest_resolution()

    try:
        video.download(VID_DIR)
    except:
        print("Download has failed. There Might be an issue")

    print('Video has been downloaded successfully')

#The main function
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-a', '--audio', required = False, help = "Downloads your audio", action = argparse.BooleanOptionalAction)
    ap.add_argument('-v', '--video', required = True, help = 'The video URL')

    args = vars(ap.parse_args())

    if args['audio']:
        Audio(args['video'])
    else:
        Video(args['video'])

if __name__ == '__main__':
    main()