from google.cloud import texttospeech

from .camera import BlindBeeCamera 


class TextToSpeech():
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
    
    def speechQR(self, txt):
        synthesis_input = texttospeech.SynthesisInput(text=txt)

        voice = texttospeech.VoiceSelectionParams(
                        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
                            )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # The response's audio_content is binary.
        with open("output123.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
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


