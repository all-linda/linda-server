from google.cloud import speech
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/service-account-file.json"

def transcribe_audio(audio_file_path):
    client = speech.SpeechClient()
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript
