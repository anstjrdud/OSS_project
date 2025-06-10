# OSS_project
2243807 - 문석영

OSS개발 SW 프로젝트입니다.

## SW 소개 및 목적
이 SW는 시간 확인 및 간단한 텍스트 파일 생성 기능과 같은 편의기능 뿐만 아니라,

한가한 시간을 보낼 수 있는 간단한 게임을 하나의 프로그램으로 통합한 것입니다.

텍스트 파일 생성과 텍스트 요약을 확인하는 기능을 한 번에 할 수 있는 등 편의기능을 하나의 프로그램으로 사용할 수 있게 하여

사용자의 편의성을 증가시킬 목적으로 이 SW를 제작하게 되었습니다.

## SW 구조, 실행 조건 및 방법
### 각 파일에 대한 설명
main.py : 메인 메뉴 구현 코드

system.py : UI 전환 기능, q키 종료 구현 코드

imports.py : 필요한 모듈 모음 코드

apps.py : 편의기능 모음 코드

games.py : 간단한 게임 모음 코드

### 필요한 모듈 및 설치 여부
psutil

keyboard

nltk

beautifulsoup4

requests

위와 같은 모듈들은 추가 설치가 필요합니다. 이는 터미널 창에 pip install (모듈 이름) 명령어를 통해서 설치합니다.

### 실행 환경
운영 체제 : Windows

코드 개발 프로그램 : Visual Studio Code

프로그래밍 언어 : Python

### 실행 방법 및 기능 설명
#### 메뉴 선택
![화면 캡처 2025-06-11 000656](https://github.com/user-attachments/assets/784e4603-8f11-44f8-a77a-d35df7b133a2)

1. 다음과 같이 메뉴가 출력된다면, 원하는 기능을 숫자로 입력해서 선택합니다. Q를 입력했다면, 프로그램을 종료합니다.

![화면 캡처 2025-06-11 002125](https://github.com/user-attachments/assets/5a793e58-6497-4e1a-bc5d-160bb499d52e)

2. 만약 게임을 선택했다면, 어떤 게임을 할 것인지 숫자로 입력해서 선택합니다. B를 입력했다면 기능 메뉴로 돌아갑니다.

#### 기능
##### 프로그램 설명
![화면 캡처 2025-06-11 012042](https://github.com/user-attachments/assets/52f9560e-9317-4868-83b2-673e0954fbe8)

프로그램에 대한 간단한 설명 및 작동 방법에 대해서 설명합니다.

##### 현재 날짜 및 시간
![화면 캡처 2025-06-11 002845](https://github.com/user-attachments/assets/6da760c8-6bb8-4a46-8c3b-556696c07599)

다음과 같이 현재 날짜와 시간을 실시간으로 출력합니다.

![화면 캡처 2025-06-11 003139](https://github.com/user-attachments/assets/e96af932-ba83-4422-a004-ec931e351e4d)

q 키를 입력한다면 다음과 같이 출력되면서, 엔터키를 누르고 메뉴로 돌아갑니다.

##### 계산기
![화면 캡처 2025-06-11 003548](https://github.com/user-attachments/assets/9eb417ac-17e3-4469-b01c-9dde03b59b3a)

말 그대로, 수식을 입력하면 계산을 하는 기능을 합니다.

![화면 캡처 2025-06-11 004104](https://github.com/user-attachments/assets/40cb213e-991a-4f4e-bded-c952911f1ac4)

예시로 든 수식을 계산할 수 있으며, 그 외에도 ceil (소수점에서 무조건 올림), floor(소수점자리 무시), round(반올림), abs(절댓값) 등의 계산도 가능합니다.

![화면 캡처 2025-06-11 004129](https://github.com/user-attachments/assets/e9841f8a-c6dc-4feb-b89f-e090e3ba41c1)

q를 입력하면, 계산기를 종료하여 메뉴로 돌아갑니다.

##### txt 파일 생성
![화면 캡처 2025-06-11 004511](https://github.com/user-attachments/assets/061b7e85-8421-4de8-9172-62445a4dba1b)

내용을 입력하여 txt 파일로 생성합니다.
우선, 파일 이름을 입력합니다. (.txt 확장명은 필요없음)
그리고, 내용을 입력합니다. 빈 줄로 입력한다면 입력을 끝내는 것입니다.

![화면 캡처 2025-06-11 004748](https://github.com/user-attachments/assets/3ed11495-895a-4993-9541-b2e584849c55)

그러면, txt 파일이 생성됩니다.
##### 시스템 정보

![화면 캡처 2025-06-11 004957](https://github.com/user-attachments/assets/9c72b41a-f2bc-46fa-ac1f-7fdb1979adc2)

컴퓨터 CPU, 메모리(RAM), 디스크, 네트워크 상태를 확인할 수 있습니다.

이는 실시간으로 갱신되며, q 키를 눌러서 메뉴로 돌아갈 수 있습니다.


##### 텍스트 요약기 (영어)
![화면 캡처 2025-06-11 005356](https://github.com/user-attachments/assets/62d7c7f7-6bbd-4e85-930a-7a26f068a844)
![화면 캡처 2025-06-11 005412](https://github.com/user-attachments/assets/fd4b7c44-5976-466d-b583-21d530be72a4)

txt 파일의 내용을 요약해서 출력합니다.

###### 실행 원리
![화면 캡처 2025-06-11 005821](https://github.com/user-attachments/assets/496850a8-c083-435d-a5f7-e07b3e509a66)

1. 입력된 텍스트를 문장 단위로 분리합니다.

2. 모든 문장을 소문자로 바꾸고 단어 단위로 토큰화, 불용어 제거, 알파벳이 아닌 단어 제거를 실행합니다.
  
3. 단어 빈도를 계산합니다.
  
4. 각 문장에 대해, 포함된 단어들의 빈도 점수 합계를 계산하고 많이 등장하는 "중요 단어"가 많을수록 점수가 높습니다.
  
5. 점수가 높은 순서대로 정렬하고, 상위 (num_sentences) 개 문장을 선택해 하나의 문자열로 연결하여 반환합니다.

#### 게임
##### 숫자 맞추기
![화면 캡처 2025-06-11 010358](https://github.com/user-attachments/assets/4fb128b2-e89d-434c-b489-2f52d890116b)

임의의 숫자를 사용자가 추측하여 맞추는 게임입니다.
##### 가위바위보
![화면 캡처 2025-06-11 010513](https://github.com/user-attachments/assets/959f06f8-db02-42de-8c2b-1c28fdacb316)

말 그대로 가위바위보를 합니다. 다시 한 번 할거면 Y(y)를, 안하고 메뉴로 돌아갈거면 N(n)을 입력합니다.
##### 단어 뒤집기
![화면 캡처 2025-06-11 010706](https://github.com/user-attachments/assets/973c18de-a7d3-4770-a65e-6d6f926affda)

제시된 단어를 얼마나 빨리 거꾸로 입력하는지 내기할 수 있습니다.
##### 틱택토
![화면 캡처 2025-06-11 011110](https://github.com/user-attachments/assets/1cf1afe0-cde2-4007-b414-cbc7bd3f4807)

3 x 3 판에서 누가 먼저 빙고를 하는지 내기합니다.
##### 행맨 (Hangman)
![화면 캡처 2025-06-11 011339](https://github.com/user-attachments/assets/bcef21fa-6730-4aa9-89e0-02657521e2cd)

철자를 추측하고 입력해서 단어를 맞춥니다.
##### 메모리 카드 맞추기
![화면 캡처 2025-06-11 011505](https://github.com/user-attachments/assets/fe99b655-c0c8-448c-8ccd-0e63d4e3d0fa)

4 x 4 판의 16개의 카드에서 8개의 짝을 맞추는 게임입니다.
##### 동전 던지기
![화면 캡처 2025-06-11 011606](https://github.com/user-attachments/assets/46390c29-277a-4916-a982-91f8f58511db)

동전의 앞뒤를 예상하고, 동전 던지기의 결과를 확인하여 예상이 맞았는지 확인합니다.

