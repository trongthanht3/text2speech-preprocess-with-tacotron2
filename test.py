from google.cloud import speech_v1 as speech


def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config, audio)
    print_sentences(response)


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print('-' * 80)
        print(f'Transcript: {transcript}')
        print(f'Confidence: {confidence:.0%}')


config = {'language_code': 'vi-VN'}
audio = {'/Users/trongthanht3/PycharmProjects/text2speech/truyenma1.mp3'}