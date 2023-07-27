import os
import time
import pygame
from google.cloud import texttospeech

# from .camera import BindBeeCamera 


class TextToSpeech():
    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json" 
        self.client = texttospeech.TextToSpeechClient()
    
    # def play_audio(self, txt):
    def play_audio(self, txt):
        # Set up google speech API
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"    # Text To Speech API
    
        # Input text to be spoken
        synthesis_input = texttospeech.SynthesisInput(text=txt)

        # Create voice
        voice = texttospeech.VoiceSelectionParams(
                        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                            )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save Audio file
        with open("temp.linear16", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "temp.linear16"')
        

        # Play Audio file
        pygame.mixer.init()
        p = pygame.mixer.Sound('/home/dspi/daAIson/main/temp.linear16')    # audio file must be 16 bits.
        p.play()
        time.sleep(10.0)
        p.stop()

    def mkaudio(self, txt):
        # Set up google speech API
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"    # Text To Speech API
    
        # Input text to be spoken
        synthesis_input = texttospeech.SynthesisInput(text=txt)

        # Create voice
        voice = texttospeech.VoiceSelectionParams(
                        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                            )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save Audio file
        # with open("temp.linear16", "wb") as out:
        with open(f"/home/dspi/daAIson/main/{txt}.linear16", "wb") as out:
            # Write t/home/dspi/daAIson/main/he response to the output file.
            out.write(response.audio_content)
            # print('Audio content written to file "temp.mp3"')
            print(f'Audio content written to file "{txt}.linear16"')
        

        # Play Audio file
        pygame.mixer.init()
        p = pygame.mixer.Sound(f'/home/dspi/daAIson/main/{txt}.linear16')    # audio file must be 16 bits.
        # p = pygame.mixer.Sound('/home/dspi/daAIson/main/temp.mp3')    # audio file must be 16 bits.
        p.play()
        time.sleep(10.0)
        p.stop()


    def translationQR(self, txt):
        # Set up google speech API
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"    # Text To Speech API
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \ /home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json" # Speech To Text API
    
        # Input text to be spoken
        synthesis_input = texttospeech.SynthesisInput(text=txt)

        # Create voice
        voice = texttospeech.VoiceSelectionParams(
                        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                            )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save Audio file
        with open("temp.linear16", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "temp.linear16"')
        
        # Play Audio file
        pygame.mixer.init()
        p = pygame.mixer.Sound('/home/dspi/daAIson/tests/temp.linear16')    # audio file must be 16 bits.
        p.play()
        time.sleep(10.0)
        p.stop()


    def testing(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
            "/home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json"
        synthesis_input = texttospeech.SynthesisInput(text="Testing Text to Speech")

        voice = texttospeech.VoiceSelectionParams(
                        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                            )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            # audio_encoding=texttospeech.AudioEncoding.MP3
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # The response's audio_content is binary.
        with open("test_tts.linear16", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "test_tts.linear16"')
        # [END tts_quickstart]

def run_quickstart():
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.
    Make sure to be working in a virtual environment.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    
    print("------Service------")
    print("[1] Detect object")
    print("[2] Register object")
    
    service = int(input("Enter the service number: "))
    
    if(service == 1):
        sentence = "Please recognize the QR code"
        print("Searching for QR code")
    elif(service == 2):
        object_name = input("Enter the name of object to be registerd: ")
        sentence = f"{object_name} is registerd at QR code 1."

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=sentence)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    
    #voice = texttospeech.VoiceSelectionParams(
    #    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    #)

    voice = texttospeech.VoiceSelectionParams(
                    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                        )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    # [END tts_quickstart]


