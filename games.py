from system import *
from imports import *

def game_a():
    number = random.randint(1, 100)
    attempts = 0
    print("숫자 맞추기 게임! 1부터 100 사이 숫자를 맞춰보세요.")

    while True:
        guess = input("숫자를 입력하세요: ")
        if not guess.isdigit():
            print("숫자를 입력해주세요.")
            continue
        guess = int(guess)
        attempts += 1

        if guess < number:
            print("더 큰 숫자입니다!")
        elif guess > number:
            print("더 작은 숫자입니다!")
        else:
            print(f"정답입니다! 시도 횟수: {attempts}번")
            break

def game_b():
    choices = ['가위', '바위', '보']
    print("가위바위보 게임! 가위, 바위, 보 중 하나를 입력하세요.")

    while True:
        user_choice = input("당신의 선택: ")
        if user_choice not in choices:
            print("가위, 바위, 보 중에서 입력해주세요.")
            continue

        comp_choice = random.choice(choices)
        print(f"컴퓨터의 선택: {comp_choice}")

        if user_choice == comp_choice:
            print("비겼습니다!")
        elif (user_choice == '가위' and comp_choice == '보') or \
             (user_choice == '바위' and comp_choice == '가위') or \
             (user_choice == '보' and comp_choice == '바위'):
            print("이겼습니다!")
        else:
            print("졌습니다!")

        if input("한 판 더? (y/n): ").lower() != 'y':
            break

def game_c():
    import random
    print("단어 뒤집기 게임! 제시된 단어를 거꾸로 입력하세요.")

    words = [
        "python", "program", "developer", "challenge", "computer",
        "notebook", "language", "internet", "variable", "function",
        "keyboard", "algorithm", "network", "terminal", "debugging"
    ]
    
    word = random.choice(words)
    reversed_word = word[::-1]

    print(f"단어: {word}")
    answer = input("거꾸로 단어를 입력하세요: ")

    if answer == reversed_word:
        print("정답입니다!")
    else:
        print(f"틀렸습니다! 정답은 {reversed_word}입니다.")


# tic_tac_toe()   

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def game_d():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = "X"

    for _ in range(9):
        print_board(board)
        row = int(input(f"{turn}'s turn - Row (0-2): "))
        col = int(input("Col (0-2): "))
        if board[row][col] != " ":
            print("잘못된 좌표입니다. 다시 해주세요.")
            continue
        board[row][col] = turn
        if check_win(board, turn):
            print_board(board)
            print(f"{turn} wins!")
            return
        turn = "O" if turn == "X" else "X"
    print("무승부입니다!")

def game_e():
    import random
    words = [
        "python", "hangman", "openai", "developer", "machine", "learning", "artificial", 
        "intelligence", "algorithm", "function", "variable", "internet", "computer", 
        "programming", "hardware", "software", "database", "debugging"
    ]
    word = random.choice(words)
    guessed = set()
    tries = 6

    while tries > 0:
        display = "".join([letter if letter in guessed else "_" for letter in word])
        print("단어:", display)

        if "_" not in display:
            print("🎉 이겼습니다!")
            return

        guess = input("철자를 추측하세요: ").lower()
        if guess in guessed:
            print("이미 추측한 철자입니다.")
        elif guess in word:
            guessed.add(guess)
        else:
            tries -= 1
            print(f"틀렸습니다. 남은 기회: {tries}")
            guessed.add(guess)

    print("졌습니다! 정답:", word)


def game_f():
    symbols = ['🍎', '🍌', '🍇', '🍒', '🍍', '🥝', '🍓', '🍉'] * 2  # 총 16개
    random.shuffle(symbols)
    board = ['*'] * 16
    matched = [False] * 16

    def show_board():
        for i in range(16):
            display = symbols[i] if matched[i] else board[i]
            print(f"{i:2}: {display}", end="   ")
            if (i + 1) % 4 == 0:
                print()
        print()

    while not all(matched):
        show_board()
        try:
            first = int(input("첫 번째 카드 번호(0~15): "))
            second = int(input("두 번째 카드 번호(0~15): "))
            if first == second or not (0 <= first < 16) or not (0 <= second < 16):
                print("잘못된 선택입니다. 범위를 확인하세요.")
                continue
            if matched[first] or matched[second]:
                print("이미 맞춘 카드입니다.")
                continue

            print(f"선택한 카드: {symbols[first]} vs {symbols[second]}")
            if symbols[first] == symbols[second]:
                matched[first] = matched[second] = True
                print("짝 맞음! 🎉")
            else:
                print("틀림! 다시 시도하세요.")
                time.sleep(1)
        except ValueError:
            print("숫자를 입력하세요.")
        except IndexError:
            print("0부터 15 사이의 숫자를 입력하세요.")
    print("🎉 모든 카드를 맞췄습니다!")

def game_g():
    choice = input("앞(Heads) 또는 뒤(Tails)를 고르세요 (h/t): ").lower()
    result = random.choice(['h', 't'])
    print("결과:", "앞 (Heads)" if result == 'h' else "뒤 (Tails)")
    if choice == result:
        print("🎉 정답!")
    else:
        print("😢 틀렸습니다.")

def run_feature_f():
    while True:
        clear_screen()
        print("\n 원하는 게임을 선택하십시오")
        print("1. 숫자 맞추기")
        print("2. 가위바위보")
        print("3. 단어 뒤집기")
        print("4. 틱택토")
        print("5. 행맨 (Hangman)")
        print("6. 메모리 카드 맞추기")
        print("7. 동전 던지기")
        print("B. 뒤로 가기")
        choice = input("선택: ")
        if choice == "1":
            clear_screen()
            game_a()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "2":
            clear_screen()
            game_b()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "3":
            clear_screen()
            game_c()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "4":
            clear_screen()
            game_d()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "5":
            clear_screen()
            game_e()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "6":
            clear_screen()
            game_f()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "7":
            clear_screen()
            game_g()
            input("엔터를 누르면 메뉴로 돌아갑니다.")
        elif choice == "b" or choice == "B":
            return