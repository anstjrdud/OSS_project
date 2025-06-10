from imports import *
from apps import *
from system import *
from games import *

stop_event = threading.Event()
        
def main_menu():
    while True:
        print("\n[ 주요 메뉴 ]")
        print('0. 프로그램 설명')
        print("1. 현재 시간")
        print("2. 계산기")
        print("3. txt 파일 생성")
        print("4. 시스템 정보")
        print("5. 텍스트 요약기 (영어)")
        print("6. 게임")
        print("Q. 종료")
        choice = input("선택: ")
        if choice == "0":
            clear_screen()
            run_feature_0()
        elif choice == "1":
            clear_screen()
            run_feature_a(stop_event)
        elif choice == "2":
            clear_screen()
            run_feature_b()
        elif choice == "3":
            clear_screen()
            run_feature_c()
        elif choice == "4":
            clear_screen()
            run_feature_d(stop_event)
        elif choice == "5":
            clear_screen()
            run_feature_e()
        elif choice == "6":
            clear_screen()
            run_feature_f()
        elif choice == "q" or choice == "Q":
            clear_screen()
            print("\n이용해주셔서 감사합니다.")
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main_menu()
