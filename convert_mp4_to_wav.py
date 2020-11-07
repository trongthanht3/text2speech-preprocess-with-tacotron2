#conver mp4 to wav
# Sampling rate: 22050
# Data format WAV Mono mean 1 channel
# Decoding PCMS16LE

import os
import re
import pysrt
from pydub import AudioSegment

#edit this path to correct data dir
def convert_mp4_to_wav(_datapath, _audiopathout):
    data_path = _datapath
    audio_path_out = _audiopathout
    sample_rate = '22050'
    channel = '1'
    for file in os.listdir(data_path):
        if (file[-3:] == 'mp4'):
            command = 'ffmpeg' + ' -i ' + data_path + '/' + file + " -ar " + sample_rate + " -ac " + channel\
                + " " + audio_path_out + '/' +  file[:-3] + 'wav'
            print(command)
            os.system(command)
            print("done!")
            command_cp = 'cp ' + data_path + '/' + file[:-3] + 'srt' + " " + audio_path_out
            os.system(command_cp)
            print("--------------------------")
    print("completed!")

#change this path for your usage
datapath = ""       #'/Users/trongthanht3/PycharmProjects/text2speech/datademo'
output = ""         #'/Users/trongthanht3/PycharmProjects/text2speech/audio_source_demo'
convert_mp4_to_wav(datapath, output)



