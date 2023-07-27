#define SPEAKER_PIN 9

void setup() {
  pinMode(SPEAKER_PIN, OUTPUT);
}

void loop() {
  tone(SPEAKER_PIN, 1000); // 1000Hz의 주파수로 소리를 내는 함수
  delay(1000); // 1초간 소리 유지
  noTone(SPEAKER_PIN); // 소리를 끕니다.
  delay(1000); // 1초간 소리를 끈 상태 유지
}