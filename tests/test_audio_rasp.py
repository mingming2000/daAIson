import RPi.GPIO as GPIO
import time
import pygame

# GPIO 핀 번호 설정 (여기서는 GPIO 17을 사용합니다. 다른 핀을 사용하려면 이 값을 바꿔주세요.)
GPIO_PIN = 17

# GPIO 설정 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 음성 파일 경로 설정 (여기서는 "sound.wav" 파일을 사용합니다. 다른 파일을 사용하려면 이 값을 바꿔주세요.)
SOUND_FILE_PATH = "test_tts.mp3"

# pygame 초기화
pygame.init()
pygame.mixer.init()

def play_sound(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print("음성 파일 재생 중 오류가 발생했습니다:", str(e))

try:
    while True:
        # GPIO 입력을 체크하고, 입력이 감지되면 음성 파일을 재생합니다.
        input_state = GPIO.input(GPIO_PIN)
        if input_state == False:
            print("음성 파일 재생을 시작합니다.")
            play_sound(SOUND_FILE_PATH)
            print("음성 파일 재생이 완료되었습니다.")
            time.sleep(0.2)  # 입력 버튼의 바운스를 방지하기 위해 잠시 대기합니다.

except KeyboardInterrupt:
    print("\n사용자에 의해 프로그램이 종료되었습니다.")
finally:
    # GPIO 설정 초기화 및 pygame 종료
    GPIO.cleanup()
    pygame.quit()
