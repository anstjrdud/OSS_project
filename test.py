import os
import time
import math
import psutil
import threading
import keyboard
import requests
from bs4 import BeautifulSoup

stop_event = threading.Event()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_time():
    try:
        clear_screen()
        while not stop_event.is_set():
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 날짜와 시간 포함
            print(f"\r현재 날짜 및 시간 : {current_time}", end='', flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
    print()


def listen_for_key():
    while not stop_event.is_set():
        if keyboard.is_pressed('q'):
            stop_event.set()
            break
        time.sleep(0.1)

def run_feature_0():
    print("\n본 프로그램에는 간단하면서 유익한 편의기능이 담겨있습니다.")
    print("일일이 따로 찾지 말고, 이 곳에 하나로 함께 사용하시길 바랍니다.")
    print("어떤 기능을 원하신다면, 선택에서 그 기능에 대응하는 숫자를 입력합니다.")
    print("그 기능을 종료하고 메뉴로 돌아가고 싶다면, q 키를 누르십시오.")
    print("이상입니다. 즐거운 프로그램 사용되십시오.")
    input("\n엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

def run_feature_a():
    stop_event.clear()
    t = threading.Thread(target=show_time)
    t.start()
    listen_for_key()
    t.join()
    print("✅ 현재 날짜 및 시간 기능을 종료합니다.")
    input("엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

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

def monitoring(interval=2):
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

def run_feature_d():
    stop_event.clear()
    t = threading.Thread(target=monitoring)
    t.start()
    listen_for_key()
    t.join()
    print("\n✅ 시스템 정보 출력을 종료합니다.")
    input("엔터를 누르면 메뉴로 돌아갑니다.")
    clear_screen()

def main_menu():
    while True:
        print("\n[ 주요 메뉴 ]")
        print('0. 프로그램 설명')
        print("1. 현재 시간")
        print("2. 계산기")
        print("3. txt 파일 생성")
        print("4. 시스템 정보")
        print("5. 종료")
        choice = input("선택: ")
        if choice == "0":
            clear_screen()
            run_feature_0()
        elif choice == "1":
            clear_screen()
            run_feature_a()
        elif choice == "2":
            clear_screen()
            run_feature_b()
        elif choice == "3":
            clear_screen()
            run_feature_c()
        elif choice == "4":
            clear_screen()
            run_feature_d()
        elif choice == "5":
            clear_screen()
            print("\n이용해주셔서 감사합니다.")
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()
