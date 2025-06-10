#from imports import *
from system import *

def run_feature_0():
    print("\n본 프로그램에는 간단하면서 유익한 편의기능이 담겨있습니다.")
    print("일일이 따로 찾지 말고, 이 곳에 하나로 함께 사용하시길 바랍니다.")
    print("어떤 기능을 원하신다면, 선택에서 그 기능에 대응하는 숫자를 입력합니다.")
    print("그 기능을 종료하고 메뉴로 돌아가고 싶다면, q 키를 누르십시오.")
    print("이상입니다. 즐거운 프로그램 사용되십시오.")
    input("\n엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

def run_feature_a(stop_event):
    stop_event.clear()
    t = threading.Thread(target=show_time, args=(stop_event,))
    t.start()
    listen_for_key(stop_event)
    t.join()
    print("✅ 현재 날짜 및 시간 기능을 종료합니다.")
    input("엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

def show_time(stop_event):
    try:
        clear_screen()
        while not stop_event.is_set():
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 날짜와 시간 포함
            print(f"\r현재 날짜 및 시간 : {current_time}", end='', flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
    print()

def run_feature_b():
    print("\n[ 계산기 기능 ]")
    print("예: 3 + 4, sqrt(25), sin(radians(30)), degrees(pi), log(100, 10)")
    print("종료하려면 'q' 입력")

    while True:
        expr = input("계산식 입력: ")
        if expr.lower() == 'q':
            print("계산기 종료")
            input("엔터를 누르면 메뉴로 돌아갑니다.")
            clear_screen()
            break
        try:
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            allowed_names.update({
                'abs': abs,
                'round': round,
                'radians': math.radians,
                'degrees': math.degrees,
            })
            result = eval(expr, {"__builtins__": None}, allowed_names)
            print(f"결과: {result}")
        except Exception as e:
            print("❌ 계산 오류:", e)


def run_feature_c():
    filename = input("저장할 파일 이름을 입력하세요 (.txt): ").strip()

    # 확장자 자동 추가
    if not filename.endswith(".txt"):
        filename += ".txt"

    print("내용을 입력하세요. (끝내려면 빈 줄 입력)")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ '{filename}' 이(가) 생성되었습니다.")
    input("엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

    

def get_size(bytes, suffix="B"):
    """바이트 단위를 읽기 쉬운 형식으로 변환"""
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

def monitoring(stop_event, interval=2):
    try:
        while not stop_event.is_set():
            clear_screen()
            print("="*30 + " 실시간 시스템 정보 " + "="*30)
            print("업데이트 시간:", time.strftime("%Y-%m-%d %H:%M:%S"))

            # CPU 정보
            print("\n[CPU]")
            print(f"사용률: {psutil.cpu_percent()}%")
            for i, perc in enumerate(psutil.cpu_percent(percpu=True)):
                print(f" - CPU {i} 사용률: {perc}%")

            # 메모리 정보
            mem = psutil.virtual_memory()
            print("\n[메모리]")
            print(f"총 메모리: {get_size(mem.total)}")
            print(f"사용 중: {get_size(mem.used)}")
            print(f"남은 메모리: {get_size(mem.available)}")
            print(f"사용률: {mem.percent}%")

            # 디스크 정보
            disk = psutil.disk_usage('/')
            print("\n[디스크]")
            print(f"총 용량: {get_size(disk.total)}")
            print(f"사용 중: {get_size(disk.used)}")
            print(f"남은 용량: {get_size(disk.free)}")
            print(f"사용률: {disk.percent}%")

            # 네트워크 정보
            net = psutil.net_io_counters()
            print("\n[네트워크]")
            print(f"전송: {get_size(net.bytes_sent)}")
            print(f"수신: {get_size(net.bytes_recv)}")

            print("\n'q' 키를 누르면 종료합니다.")
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n모니터링을 종료합니다.")

def run_feature_d(stop_event):
    stop_event.clear()
    t = threading.Thread(target=monitoring, args=(stop_event,))

    t.start()
    listen_for_key(stop_event)
    t.join()
    print("\n✅ 시스템 정보 출력을 종료합니다.")
    input("엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

def summarize_text(text, num_sentences=3):
    # 문장 분리
    sentences = sent_tokenize(text)
    # 단어 분리 및 소문자 변환
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    # 알파벳 단어만 남기기
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # 단어 빈도 계산
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1

    # 문장별 점수 계산 (빈도 합)
    sentence_scores = {}
    for sent in sentences:
        sent_words = word_tokenize(sent.lower())
        score = 0
        for w in sent_words:
            if w in freq:
                score += freq[w]
        sentence_scores[sent] = score

    # 점수 높은 문장 상위 num_sentences개 반환
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summary_sentences)



def run_feature_e():
    file_path = input('요약할 텍스트 파일의 이름을 입력하십시오. (.txt 확장명 포함할 것) :')

    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print("요약 결과:")
    print(summarize_text(text))
    input("엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()