import pysrt
from pydub import AudioSegment

audio_name = 'ma_bup_be.mp3'
sub_name = 'ma_bup_be.srt'
audio_outdir = 'audios'
csv_output = 'output.csv'

song = AudioSegment.from_file(audio_name)
subs = pysrt.open(sub_name, encoding='utf-8')

# Define lambda function convert time to miliseconds
time_to_ms = lambda x: (x.hours*3600 + x.minutes * 60 + x.seconds) * 1000 + x.milliseconds

# Extract data
with open(csv_output, 'w') as fd:
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
        fd.append('{}|{}\n'.format(audio_extract_name, text))