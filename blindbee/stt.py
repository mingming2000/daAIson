import argparse

import os
import os.path as path
from google.cloud import speech
from pydub import AudioSegment

# Speech To Text API
# $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"

class SpeechToText():
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
            "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"
        self.client = speech.SpeechClient()

    def record(self):
        """
        """

    def transcribe_audio_to_text(self, speech_file: str) -> speech.RecognizeResponse:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
            "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"
        """Transcribe the given audio file."""

        # read audio file
        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()


        # Transcribe Audio to Text
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            # sample_rate_hertz=16000,
            language_code="en-US",
        )
        response = self.client.recognize(config=config, audio=audio)

        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        text = None
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print(f"Transcript: {result.alternatives[0].transcript}")
            text = f'{result.alternatives[0].transcript} '

        return text

    def testing(self) -> speech.RecognizeResponse:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
            "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"
        """Transcribe the given audio file."""

        # read audio file
        
        # Not working on MP3!!!!!
        speech_file = "/home/dspi/daAIson/tests/test_tts.linear16"
        

        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()


        # Transcribe Audio to Text
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            #sample_rate_hertz=16000,   # Do not change!!
            language_code="en-US",
        )
        response = self.client.recognize(config=config, audio=audio)

        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            print(f"Transcript: {result.alternatives[0].transcript}")

        return response  
