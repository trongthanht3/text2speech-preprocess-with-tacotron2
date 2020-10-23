#This script will use autosub to generate text from audio
#------------
#autosub version install from pip maybe won't work
#you can try this:
#pip install git+https://github.com/BingLingGroup/autosub
#
#my data wrote in vietnamese so it may error sometime
#so i just rename it with no_accent_vietnamese()
#
#how to config this?
#   data_path = data-dir (where you save your data)
#   sapi = api-for-speech-to-text (default is gsv2)
#   lang_code = language-code
#check autosub's github to learn more
#


import os
import re

data_path = '/Users/trongthanht3/PycharmProjects/text2speech/data'
sapi = 'gsv2'      #read git of autosub to learn more gcsv1=google-speech-api
lang_code = 'vi-VN'

def no_accent_vietnamese(s):
    s = s.lower()
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'o', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'i', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'u', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    s = re.sub('[ \b\t]', '_', s)
    return s

#rename to make sure there's no space or special char in file name
def file_rename(data_path):
    for file in os.listdir(data_path):
        new_name = no_accent_vietnamese(file)
        print(new_name)
        os.rename(data_path+'/'+file, data_path+'/'+new_name)

#we need to rename sub file after gen sub
#because autosub add lang_code to end of file name
#then we can use sub to generate csv
def file_rename_after(data_path):
    for file in os.listdir(data_path):
        if (file[-3:] == 'srt'):
            os.rename(data_path+'/'+file, data_path+'/'+file[:-9]+"srt")

def autosub_gen_srt(data_path, sapi, lang_code):
    print("start generate sub from audio")
    for file in os.listdir(data_path):
        #check if sub exist
        print("renaming: ", file)
        name = file[:-3]+'.srt'
        if os.path.isfile(data_path+'/'+name):
            print("sub existed!")
            print("---------------------------")
            continue
        elif (file[-3:] != 'mp4'):
            print("wrong file type!")
            print("---------------------------")
            continue
        else:
            command = 'autosub' + ' -i ' + data_path + '/' + file + ' -sapi ' + sapi\
                + ' -S ' + lang_code
            print(command)
            os.system(command)
            print("done!")
        print("---------------------------")



# file_rename(data_path)
autosub_gen_srt(data_path, sapi, lang_code)
file_rename_after(data_path)
print("gen completed!")