import os
import re
import pysrt
import pandas as pd
from pydub import AudioSegment

#rename filename for vietnamese
#sửa lại tên file để loại bỏ dấu câu với những file có tên tiếng việt
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

#generate all your data to a csv
#generate toàn bộ data và gom về 1 file csv có dạng:
#   path_to_audio|<text content>

#generate_csv will gen csv for 1 file only
#hàm dưới chỉ gen csv cho 1 file
def generate_csv(_audioname, _subname, _audiooutdir, _csvoutput):
    audio_name = _audioname     #'ma_bup_be.mp3'
    sub_name = _subname         #'ma_bup_be.srt'
    audio_outdir = _audiooutdir #'audios'
    csv_output = _csvoutput     #'output.csv'

    song = AudioSegment.from_file(data_path + '/' + audio_name)
    subs = pysrt.open(data_path + '/' + sub_name, encoding='utf-8')

    # Define lambda function convert time to miliseconds
    time_to_ms = lambda x: (x.hours*3600 + x.minutes * 60 + x.seconds) * 1000 + x.milliseconds

    # Extract data
    mode_export = 'w'
    if (os.path.isfile('meta_data.csv')):
        mode_export = 'a'
    with open(csv_output, mode=mode_export) as fd:
        for sub in subs:
            # Get start time, end time in miliseconds
            start_ms = time_to_ms(sub.start)
            end_ms = time_to_ms(sub.end)
            # Audio extracted file name
            audio_extract_name = '{}/{}_{}_{}.wav'.format(audio_outdir, audio_name, start_ms, end_ms)
            text = str(sub.text)
            # Extract file
            extract = song[start_ms:end_ms]
            # Saving
            extract.export(audio_extract_name, format="wav")
            # Write to csv file
            fd.write('{}|{}\n'.format(audio_extract_name, text))

#this function will append all csv to 1
#hàm dưới sẽ gom hết các csv về 1 file lớn
#nếu chỉ cần generate cho 1 file nhỏ lẻ, chỉ dùng hàm trên sau đó nối với nhau bằng pandas sẽ tốt hơn
#hàm dưới để tự động hoá hơn với 1 khối dữ liệu lớn
def generate_csv_dir(data_path, output_path):
    # print("the fuck bro!")
    for file in os.listdir(data_path):
        if (file[-3:] == 'wav'):
            print("Adding: ", file)
            sub_path = data_path + '/' + file[:-3]+'srt'
            # if (os.path.isfile('meta_data.csv')):
            #     csv_output = 'meta_data_temp.csv'
            if (os.path.isfile(sub_path)):
                audio_name = file  # 'ma_bup_be.mp3'
                sub_name = file[:-3]+'srt'  # 'ma_bup_be.srt'
                audio_outdir = output_path  # 'audios'
                csv_output = 'meta_data.csv'  # 'output.csv'
                generate_csv(audio_name, sub_name, audio_outdir, csv_output)
            else:
                print(sub_path)
                print("sub file not exist!")
            # if (os.path.isfile('meta_data_temp.csv')):
            #     meta = pd.read_csv('meta_data.csv')
            #     meta_temp = pd.read_csv('meta_data_temp.csv')
            #     meta.append(meta_temp)
            #     meta.to_csv(sep='|')


#change path for your usage / đổi path dưới đây theo đúng đường dẫn trên máy

#data directory: put all your data (sub, audio file) to this folder
#đặt toàn bộ sub, audio tương ứng đã xử lý vào 1 folder,
#thay đổi đường dẫn dưới tới folder đó
data_path = '/Users/trongthanht3/PycharmProjects/text2speech/audio_source_demo'

#output folder
#folder để chứa data output
output_path = '/Users/trongthanht3/PycharmProjects/text2speech/audios_demo'

#gen csv cho toàn bộ dữ liệu
generate_csv_dir(data_path, output_path)



