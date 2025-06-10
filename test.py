import os
import time
import math
import threading
import keyboard

stop_event = threading.Event()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_time():
    while not stop_event.is_set():
        print("\r현재 시간 : " + time.strftime("%H:%M:%S"), end='', flush=True)
        time.sleep(1)
    print()

def listen_for_key():
    print("\n작업 실행 중... 'q'를 누르면 종료됩니다.")
    while not stop_event.is_set():
        if keyboard.is_pressed('q'):
            stop_event.set()
            break
        time.sleep(0.1)

def run_feature_a():
    stop_event.clear()
    t = threading.Thread(target=show_time)
    t.start()
    listen_for_key()
    t.join()
    print("✅ 기능 A 종료 완료")
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

def main_menu():
    while True:
        print("\n[ 주요 메뉴 ]")
        print("1. 현재 시간")
        print("2. 계산기")
        print("3. 종료")
        choice = input("선택: ")
        if choice == "1":
            clear_screen()
            run_feature_a()
        elif choice == "2":
            clear_screen()
            run_feature_b()
        elif choice == "3":
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()
